from models import *
from application_interface import ApplicationInterface

# adds uniqe applicaton codes to those who doesnt have
Applicant.generate_uniqe(Applicant.find_missing_pk())

# finds the closest school based on the city where the applicant lives (for everyone)
Applicant.find_school(Applicant.find_missing_city())

# appoints an interview for all the new applicants, changing their status, and filling an interview slot
Applicant.appoint_interview(Applicant.find_missing_interview())

# user interface
number = ApplicationInterface.choose_applicant()
user = ApplicationInterface(number)
user.print_menu()
user.run_option(user.option())
