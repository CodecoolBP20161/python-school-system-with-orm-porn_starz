from models import *

class AdminInterface():

    @staticmethod
    def print_menu():
        print('''Welcome to the admin system of CodeCool!
Please choose an option!
(1) Maintenance
(2) Check applicants
(3) Questions'''
)
    @staticmethod
    def choose_an_option():
        number_of_choose = input('Give me a number: ')
        return number_of_choose

    @staticmethod
    def option(number):

        if number == '1':
            # adds uniqe applicaton codes to those who doesnt have
            Applicant.generate_uniqe(Applicant.find_missing_pk())

            # finds the closest school based on the city where the applicant lives (for everyone)
            Applicant.find_school(Applicant.find_missing_city())

            # appoints an interview for all the new applicants, changing their status, and filling an interview slot
            Applicant.appoint_interview(Applicant.find_missing_interview())

        if number == '2':
            run = True
            while run:
                print('''Choose a filter:
     (1) name
     (2) Status
     (3) App. number
     (4) City
     (5) Email
     (6) School
     (x) Exit''')

                x = input('Choose an option: ')
                if x == 'x':
                    run = False
                else:
                    y = input('Choose a filter: ')

                if x == '1':
                    all_data = Applicant.filter(Applicant.name, y)
                if x == '2':
                    all_data = Applicant.filter(Applicant.status, y)
                if x == '3':
                    all_data = Applicant.filter(Applicant.application_number, y)
                if x == '4':
                    all_data = Applicant.filter(Applicant.city, y)
                if x == '5':
                    all_data = Applicant.filter(Applicant.email, y)
                if x == '6':
                    all_data = Applicant.filter(Applicant.school, y)

                filtered_table = PrettyTable(["Name", "Status", "App. number", "City", "Email", "School"])
                filtered_table.align["Name"] = "l"  # Left align city names
                filtered_table.padding_width = 1    # One space between column edges and contents (default)
                for student in all_data:
                    filtered_table.add_row(student)
                print(filtered_table)
