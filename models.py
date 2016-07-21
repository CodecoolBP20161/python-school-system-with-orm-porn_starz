from peewee import *
import string
import random

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
    def find_school(cls, instances):
        for instance in instances:
            the_city = City.select().where(City.name == instance.city)[0]  # sooo not pretty
            the_school = School.select().where(the_city.closest_school.name == School.name)[0]
            instance.school = the_school.name
            instance.save()

    @classmethod
    def generate_uniqe(cls, instances):
        for instance in instances:
            found = False
            while not found:
                uniqe = []
                for x in range(12):
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
    def appoint_interview(cls, instances):
        for instance in instances:
            mentor_to_meet = random.choice(Mentor.select().where(instance.school.name == Mentor.school))
            first_possible = InterviewSlot.select().where(
                mentor_to_meet.mentor_id == InterviewSlot.mentor, InterviewSlot.applicant >> None
                ).order_by(
                InterviewSlot.time
                )[0]
            instance.status = "In progress"
            first_possible.applicant = instance
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


class Mentor(BaseModel):

    name = CharField()
    mentor_id = PrimaryKeyField()
    school = ForeignKeyField(School)


class InterviewSlot(BaseModel):

    mentor = ForeignKeyField(Mentor)
    time = DateField()
    applicant = ForeignKeyField(Applicant, null=True)
