from models import *
from prettytable import PrettyTable


class ApplicationInterface():

    # @staticmethod
    # def send_email():
    #     import smtplib
    #     # SERVER = "localhost"
    #
    #     FROM = 'toth910719balint@gmail.com'
    #
    #     TO = ["toth910719balint@gmail.com'"]  # must be a list
    #
    #     SUBJECT = "a"
    #
    #     TEXT = "This message was sent with Python's smtplib."
    #
    #     # Prepare actual message
    #
    #     message = """\
    #     From: %s
    #     To: %s
    #     Subject: %s
    #
    #     %s
    #     """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    #
    #     # Send the mail
    #
    #     server = smtplib.SMTP()
    #     server.sendmail(FROM, TO, message)
    #     server.quit()

    @staticmethod
    def choose_applicant():
        application_number = input("Log in with applicaton number: ")
        return application_number

    def __init__(self, number):

        self.application_number = number
        self.applicaton = Applicant.get(Applicant.application_number == number)

    def print_menu(self):
        print('''
Welcome to the applicaton system of CodeCool!
Please choose an option!
(1) Application details
(2) Interview Details
(3) My questions
(4) Find my mentors
''')

    def option(self):
        option = input("")
        return option

    def print_result(self, query_result):
        for data in query_result:
            print(data)

    def run_option(self, option):
        if option == '1':
            self.print_result(Applicant.find_status(self.application_number))
        if option == '2':
            self.print_result(Applicant.find_interview(self.application_number))
        if option == '3':
            self.print_result(Applicant.find_questions(self.application_number))
        if option == '4':
            self.print_result(self.applicaton.get_mentors())
