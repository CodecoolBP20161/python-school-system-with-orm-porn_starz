from models import *
from datetime import date, time


bp1 = School.create(
    name='BP1'
)

bp2 = School.create(
    name='BP2'
)

miskolc1 = School.create(
    name='Miskolc1'
)

City.create(
    name='Horcsoghalom',
    closest_school=miskolc1
)

City.create(
    name='Karancspuszta',
    closest_school=miskolc1
)

City.create(
    name='Budapest',
    closest_school=bp1
)

nintendo = Applicant.create(
    name='Lakatos Nintendo',
    city='Karancspuszta',
    email='sukargyerek@gmail.com'
)

shakira = Applicant.create(
    name='Kolompar Shakira',
    city='Horcsoghalom',
    email='sukarlejany@gmail.com',
    )

Applicant.create(
    name='Orban Gaspar',
    city='Budapest',
    email='nemkozszereplo@gmail.com',
    )

padlab = Mentor.create(
    name='Padlab Ormester',
    school=bp1
)

joska = Mentor.create(
    name='Joska bacsi',
    school=bp2
)

bela = Mentor.create(
    name='A Bela',
    school=miskolc1
)

InterviewSlot.create(
    mentor=padlab,
    time=date(2016, 10, 10)
)

InterviewSlot.create(
    mentor=padlab,
    time=date(2016, 10, 11)
)

InterviewSlot.create(
    mentor=padlab,
    time=date(2016, 10, 12)
)

InterviewSlot.create(
    mentor=joska,
    time=date(2016, 10, 10)
)

InterviewSlot.create(
    mentor=joska,
    time=date(2016, 10, 11)
)

InterviewSlot.create(
    mentor=joska,
    time=date(2016, 10, 12)
)

InterviewSlot.create(
    mentor=bela,
    time=date(2016, 10, 10)
)

InterviewSlot.create(
    mentor=bela,
    time=date(2016, 10, 11)
)

InterviewSlot.create(
    mentor=bela,
    time=date(2016, 10, 12)
)

QuestionAnswer.create(
    applicant=nintendo,
    question='Hello, what is your name?'
)

QuestionAnswer.create(
    applicant=nintendo,
    question='Hello, what is my name?'
)

QuestionAnswer.create(
    applicant=shakira,
    question='Hello?'
)
