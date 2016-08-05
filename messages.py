from config import *


greetings = '''Dear %s!

Thank you for your applicaton to Codecool.Your application code is "%s".
The closest school to your location is %s, which is in %s.

See you soon!

Cheers!
Mentors
'''

information_for_applicant = ''' Dear %s!

You will have an interview at %s, where your mentors will be %s, and %s!

See you soon!

Cheers!
Mentors'''

information_for_mentor = '''Dear %s!

You will have an interview at %s with our new applicant, who's name is %s!

Cheers!
CodecoolRobot!'''


def send_email(address, message):
    import smtplib

    server = smtplib.SMTP(smtp, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromemail, password)
    server.sendmail(fromemail, address, message)
