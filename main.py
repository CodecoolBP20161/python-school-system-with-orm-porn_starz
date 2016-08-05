from user import user_interface
from admin import admin_interface
from os import system


def main():
    try:
        from prettytable import PrettyTable
    except ImportError:
        install = input(
            "In order to Run the program, you need to install the Prettytable python module.Install it?(y/n)")
        if install == 'y':
            system('sudo pip install prettytable')
        else:
            print('The program will quit now.')
            raise SystemExit
    choice = input('''
Please choose your role:
1.Admin
2.Applicant\n''')

    if choice == "1":
        admin_interface()
    elif choice == "2":
        user_interface()

main()
