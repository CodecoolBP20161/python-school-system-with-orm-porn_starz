from models import *
from datetime import date, time


bp1 = School.create(
    name='BP1',
    location='Budapest'
)

bp2 = School.create(
    name='BP2',
    location='Budapest'
)

miskolc1 = School.create(
    name='Miskolc1',
    location='Miskolc'
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

City.create(
    name='Vac',
    closest_school=bp2

)
City.create(
    name='Szazhalombatta',
    closest_school=bp2

)

surnames = ['Smith', 'Anderson', 'Clark', 'Wright', 'Mitchell', 'Johnson', 'Thomas', 'Rodriguez', 'Lopez', 'Perez',
            'Williams', 'Jackson', 'Lewis', 'Hill', 'Roberts', 'Jones', 'White', 'Lee', 'Scott', 'Turner', 'Brown',
            'Harris', 'Walker', 'Green', 'Phillips', 'Davis', 'Martin', 'Hall', 'Adams', 'Campbell', 'Miller',
            'Thompson',  'Allen', 'Baker', 'Parker', 'Wilson', 'Garcia', 'Young', 'Gonzalez', 'Evans', 'Moore',
            'Martinez', 'Hernandez', 'Nelson', 'Edwards', 'Taylor', 'Robinson', 'King', 'Carter', 'Collins']

first_names = ['James', 'Christopher', 'Ronald', 'Mary', 'Lisa', 'Michelle', 'John', 'Daniel', 'Anthony',
               'Patricia', 'Nancy', 'Laura',
               'Robert', 'Paul', 'Kevin', 'Linda', 'Karen', 'Sara', 'Michael',
               'Mark', 'Jason', 'Barbara', 'Betty', 'Kimberly', 'William', 'Donald', 'Jeff', 'Elizabeth',
               'Helen', 'Debora', 'David',
               'George', 'Jennifer', 'Sandra', 'Richard', 'Kenneth', 'Maria',
               'Donn', 'Charles', 'Steven', 'Susan', 'Caro', 'Josephine', 'Edward',
               'Margaret', 'Ruth', 'Thomas', 'Brian', 'Dorothy', 'Sharon']

cities = ["Karancspuszta", "Horcsoghalom", "Budapest", 'Vac', 'Szazhalombatta']

schools = [bp1, bp2, miskolc1]

words = ['pseudoartistically', 'irresolvable', 'unexplicated', 'unsensitising', 'unshriven', 'reminisce', 'byzas',
         'pavillon', 'nielloed', 'photophobia', 'tautology', 'flout', 'bourbon', 'seton', 'diminished', 'passivism',
         'nerol', 'goosewing', 'vaunted', 'tellingly', 'sidrah', 'philipsburg', 'preshared', 'collier', 'excusable',
         'rosario', 'unpouched', 'roupily']

# Creating lots of random mentors to work with
mentors = []
for x in range(21):
    if x <= 7:
        school = bp1
    elif x <= 14:
        school = bp2
    else:
        school = miskolc1
    surname = random.choice(surnames)
    first_name = random.choice(first_names)
    email = str(surname[:3] + first_name[:3])
    new_mentor = Mentor.create(
        name=surname + " " + first_name,
        school=school,
        email="codecoolrobot+%s@gmail.com" % email
    )
    mentors.append(new_mentor)

# Creating a lots of random applicants to work with
applicants = []
for y in range(2000):
    city = random.choice(cities)
    surname = random.choice(surnames)
    first_name = random.choice(first_names)
    email = str(surname[:3] + first_name[:3])
    applicant = Applicant.create(
        name=surname + " " + first_name,
        city=city,
        email="codecoolrobot+%s@gmail.com" % email
        )
    applicants.append(applicant)

hour = 9
day = 10
interview_slots = []
# Creating interview time slots
while hour != 14 and day != 14:
    new_slot = InterviewSlot.create(
        date=date(2016, 10, day),
        time=time(hour, 0)
    )
    interview_slots.append(new_slot)
    hour += 1
    if hour == 14:
        day += 1
        hour = 9
# assigning the mentors to each date
for mentor in mentors:
    for slot in interview_slots:
        SlotMentor.create(
            mentor=mentor,
            slot=slot
        )

# Creating random questions to work with
for z in range(1000):
    question = [random.choice(words) for k in range(random.randint(3, 7))]
    question = " ".join(question) + '?'
    question = question[0].capitalize() + question[1:]
    QuestionAnswer.create(
        applicant=random.choice(applicants),
        question=question,
        date=date(2016, random.randint(7, 8), random.randint(1, 29))
    )
