from getpass import getpass
from prettytable import PrettyTable
from models import Applicant, InterviewSlot, Mentor, Interview
import sys
import datetime

class AdminInterface():

    @staticmethod
    def log_in():
        password = "bela"
        pw = getpass("Password: ")
        return password == pw

    def run(self):
        self.on = True
        while self.on:
            option = self.choose()
            if option is '1':
                self.maintenance()
            if option is '2':
                self.list_them()
            if option is '3':
                self.list_interviews()
            if option is 'x':
                sys.exit()

    def choose(self):
        print('Admin interface\n\n(1) Maintenance\n(2) Applicants\n(3) Interviews\n(x) Exit')
        return input("Choose: ")

    def maintenance(self):
        print("Generating application numbers...")
        # adds uniqe applicaton codes to those who doesnt have
        Applicant.generate_uniqe(Applicant.find_missing_pk())
        print("Application numbers are generated")

        print("Searching for schools for applicants...")
        # finds the closest school based on the city where the applicant lives (for everyone)
        Applicant.find_school(Applicant.find_missing_city())
        print("Search completed.")

        print("Appointing interviews...")
        # appoints an interview for all the new applicants, changing their status, and filling an interview slot
        Applicant.appoint_interview(Applicant.find_missing_interview())
        print("Done.")

    def list_them(self):
        print('(0) All\n(1) Name\n(2) Status\n(3) App number\n(4) City\n(5) Email\n(6) School\n(x) Back')
        try:
            choose = int(input("Choose: "))
            table = PrettyTable(['Name', 'Status', 'App number', 'City', 'Email', 'School'])
            table.padding_width = 1
            if choose is 0:
                all_data = Applicant.filter()
            else:
                write = input("Choose: ")
                if choose is 1:
                    all_data = Applicant.filter(Applicant.name, write)
                if choose is 2:
                    all_data = Applicant.filter(Applicant.status, write)
                if choose is 3:
                    all_data = Applicant.filter(Applicant.application_number, write)
                if choose is 4:
                    all_data = Applicant.filter(Applicant.city, write)
                if choose is 5:
                    all_data = Applicant.filter(Applicant.email, write)
                if choose is 6:
                    all_data = Applicant.filter(Applicant.school, write)
            for student in all_data:
                table.add_row(student)
            print(table)
        except:
            pass

    def list_interviews(self):
        print('(0) All\n(1) Applicant\n(2) Time\n(3) Hour\n(4) Mentor\n(5) School\n(x) Back')
        # try:
        choose = int(input("Choose: "))
        table = PrettyTable(['School', 'Date', 'Time', 'Applicant', 'M1', 'M2'])
        table.padding_width = 1
        if choose is 0:
            all_data = Interview.get_interviews()
        # else:
        #     write = input("Choose: ")
        #     if choose is 1:
        #         all_data = InterviewSlot.filter(Applicant.name, write)
        #     if choose is 2:
        #         write = write.split("-")
        #         y = int(write[0])
        #         m = int(write[1])
        #         d = int(write[2])
        #         all_data = InterviewSlot.filter(InterviewSlot.time, datetime.date(y, m, d))
        #     if choose is 3:
        #         all_data = InterviewSlot.filter(InterviewSlot.hour, datetime.time(int(write)))
        #     if choose is 4:
        #         all_data = InterviewSlot.filter(Mentor.name, write)
        #     if choose is 5:
        #         all_data = InterviewSlot.filter(Mentor.school, write)
        for student in all_data:
            table.add_row(student)
        print(table)
        # except:
        #     pass
