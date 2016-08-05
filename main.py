from user import user_interface
from admin import admin_interface


def main():
    choice = input('''
    Please choose your role:
    1.Admin
    2.Applicant''')

    if choice == "1":
        admin_interface()
    elif choice == "2":
        user_interface()
