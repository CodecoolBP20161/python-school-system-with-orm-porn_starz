from models import *

db.connect()
db.drop_tables([School, City, Applicant, Mentor, InterviewSlot, SlotMentor, Interview, QuestionAnswer], safe=True)
db.create_tables([School, City, Applicant, Mentor, InterviewSlot, SlotMentor, Interview, QuestionAnswer], safe=True)
