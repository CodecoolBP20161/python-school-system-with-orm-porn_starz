from models import *

class ApplicationInterface():

    @staticmethod
    def choose_applicant():
        application_number = input("Log in with applicaton number: ")
        return application_number

    def __init__(self, number):

        self.application_number = number

    def print_menu(self):
        print('''Welcome to the applicaton system of CodeCool!
        Please choose an option!
        (1) Application details''')

    def option(self):
        option = input("")
        return option

    def print_result(self, query_result):
        print(query_result[0] + " ---> " + query_result[1])

    def run_option(self, option):
        if option == '1':
            self.print_result(Applicant.find_status(self.application_number))
