from models import *

class AdminInterface():

    @staticmethod
    def print_menu():
        print('''Welcome to the admin system of CodeCool!
Please choose an option!
(1) Maintenance
(2) Check applicants
(3) rizzsel'''
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
            akarmi = True
            while akarmi:
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
                    akarmi = False
                else:
                    y = input('Choose a filter: ')

                if x == '1':
                    Applicant.filter(Applicant.name, y)
                if x == '2':
                    Applicant.filter(Applicant.status, y)
                if x == '3':
                    Applicant.filter(Applicant.application_number, y)
                if x == '4':
                    Applicant.filter(Applicant.city, y)
                if x == '5':
                    Applicant.filter(Applicant.email, y)
                if x == '6':
                    Applicant.filter(Applicant.school, y)
