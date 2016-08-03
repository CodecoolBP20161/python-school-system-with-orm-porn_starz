from models import *
from application_interface import ApplicationInterface


# user interface
number = ApplicationInterface.choose_applicant()
user = ApplicationInterface(number)
user.print_menu()
user.run_option(user.option())
