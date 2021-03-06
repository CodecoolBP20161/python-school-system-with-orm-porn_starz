from models import *
from prettytable import PrettyTable


class ApplicantInterface():

    @staticmethod
    def choose_applicant():
        application_number = input("Log in with applicaton number: ")
        return application_number

    def __init__(self, number):

        self.application_number = number

    def print_menu(self):
        print('''
Welcome to the applicaton system of CodeCool!
Please choose an option!
(1) Application details
(2) Interview Details
(3) My questions
''')

    def option(self):
        option = input("")
        return option

    def print_result(self, query_result):
        table = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
        for data in query_result:
            table.row

    def run_option(self, option):
        if option == '1':
            self.print_result(Applicant.find_status(self.application_number))
        if option == '2':
            self.print_result(Applicant.find_interview(self.application_number))
        if option == '3':
            self.print_result(Applicant.find_questions(self.application_number))
