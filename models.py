from peewee import *
import string
import random
import datetime

db = PostgresqlDatabase('TothBalint', user='balint')


class BaseModel(Model):
    class Meta:
        database = db


class School(BaseModel):

    name = CharField(primary_key=True)


class City(BaseModel):

    name = CharField(primary_key=True)
    closest_school = ForeignKeyField(School)


class Applicant(BaseModel):

    basic_id = PrimaryKeyField()
    application_number = CharField(unique=True, null=True)
    name = CharField()  # given
    city = CharField()  # given
    status = CharField(default='New')
    email = CharField()  # given
    school = ForeignKeyField(School, null=True)

    @classmethod
    def find_status(cls, number):
        applicant = cls.select().where(cls.application_number == number)[0]
        applicant_status = applicant.status
        applicant_school = applicant.school.name
        return [applicant_school, applicant_status]

    @classmethod
    def find_school(cls, instances):
        for instance in instances:
            the_city = City.select().where(City.name == instance.city)[0]
            the_school = School.select().where(the_city.closest_school.name == School.name)[0]
            instance.school = the_school.name
            instance.save()

    @classmethod
    def generate_uniqe(cls, instances):
        for instance in instances:
            found = False
            while not found:
                uniqe = []
                for x in range(5):
                    letter = random.choice(list(string.ascii_lowercase))
                    uniqe.append(letter)
                uniqe = "".join(uniqe)
                try:
                    cls.select().where(cls.application_number == uniqe)[0]
                except:
                    found = True
            instance.application_number = uniqe
            instance.save()

    @classmethod
    def filter(cls, filt=None, data=None):
        all_data = []
        applicants = cls.select().where(filt == data)
        for app in applicants:
            all_data.append([app.name, app.status, app.application_number, app.city, app.email, app.school.name])
        return all_data

    @classmethod
    def appoint_interview(cls, instances):
        for instance in instances:
            slot = random.choice(InterviewSlot.select().join(SlotMentor).where(cls.school == SlotMentor.mentor.school))
            mentor_to_meets = random.choice(Mentor.select().where(instance.school.name == Mentor.school))
            first_possible = InterviewSlot.select().where(
                mentor_to_meet.mentor_id == InterviewSlot.mentor, InterviewSlot.applicant >> None
                ).order_by(
                InterviewSlot.time
                )[0]
            instance.status = "In progress"
            slot.applicant = instance
            instance.save()
            first_possible.save()

    @classmethod
    def find_missing_pk(cls):
        return cls.select().where(cls.application_number >> None)

    @classmethod
    def find_missing_city(cls):
        return cls.select().where(cls.school >> None)

    @classmethod
    def find_missing_interview(cls):
        return cls.select().where(cls.status == 'New')

    @classmethod
    def find_interview(cls, number):
        app = cls.select().join(InterviewSlot).join(Mentor).where(cls.application_number == number).get()
        slot = InterviewSlot.select().join(cls).where(cls.application_number == number).get()
        men = Mentor.select().join(InterviewSlot, JOIN.RIGHT_OUTER).join(cls).where(cls.application_number == number).get()
        return [app.school_id, slot.time, slot.hour, men.name]

    @classmethod
    def find_questions(cls, number):
        questions = []
        query = QuestionAnswer.select().join(cls).where(cls.application_number == number)
        for question in query:
            q = question.get()
            q_infos = [q.question, q.status, q.answer]
            questions.append(q_infos)
        return questions

    @classmethod
    def find_mentors(cls, number):
        mentors = Mentor.select().join(City, on=City.closest_school == Mentor.school).join(cls, on=City.name == Applicant.city).where(cls.application_number == number)
        return [mentor.name for mentor in mentors]

    def get_mentors(self):
        mentors = Mentor.select().join(
            City, on=City.closest_school == Mentor.school
        ).join(
            self.__class__, on=City.name == self.__class__.city
        ).where(self.__class__.application_number == self.application_number)
        return [mentor.name for mentor in mentors]


class Mentor(BaseModel):

    name = CharField()
    mentor_id = PrimaryKeyField()
    school = ForeignKeyField(School)
    email = CharField()


class InterviewSlot(BaseModel):

    slot_id = PrimaryKeyField()
    date = DateField()
    time = TimeField()

    # @classmethod
    # def filter(cls, filt=None, data=None):
    #     all_data = []
    #     query = (
    #         cls
    #         .select(cls, Mentor, Applicant)
    #         .join(Mentor)
    #         .join(Applicant, JOIN.LEFT_OUTER, on=InterviewSlot.applicant == Applicant.basic_id)
    #         .where(filt == data))
    #     for all_info in query:
    #         data = [str(all_info.mentor.name), str(all_info.mentor.school.name), str(all_info.time), str(all_info.hour)]
    #         try:
    #             data.append(str(all_info.applicant.name))
    #         except:
    #             data.append(None)
    #         all_data.append(data)
    #     return all_data


class SlotMentor(BaseModel):

    SM_id = PrimaryKeyField()
    mentor = ForeignKeyField(Mentor)
    slot = ForeignKeyField(InterviewSlot)
    applicant = ForeignKeyField(Applicant)


class Interview(BaseModel):

    int_id = PrimaryKeyField()
    applicant = ForeignKeyField(Applicant)
    slot = ForeignKeyField(InterviewSlot)


class QuestionAnswer(BaseModel):

    applicant = ForeignKeyField(Applicant)
    question = CharField()
    answer = CharField(default=None, null=True)
    status = CharField(default='New')
    mentor = ForeignKeyField(Mentor, null=True)
    date = DateField()
