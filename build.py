from models import *

db.connect()
# db.drop_tables([], safe=True)  # for testing
db.create_tables([School, City, Applicant, Mentor, InterviewSlot], safe=True)
