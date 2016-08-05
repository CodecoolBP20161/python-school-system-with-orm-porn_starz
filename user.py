from models import *
from applicant_interface import ApplicantInterface


# user interface
number = ApplicantInterface.choose_applicant()
user = ApplicantInterface(number)
user.print_menu()
user.run_option(user.option())
