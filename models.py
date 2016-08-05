from peewee import *
import string
import random
import datetime
import messages

from prettytable import PrettyTable

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

    def send_email(self, message):
        import smtplib

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('codecoolrobot@gmail.com', 'codecoolrobot1')
        server.sendmail("codecoolrobot@gmail.com", self.email, message)

    @classmethod
    def filter(cls, filt=None, data=None):
        all_data = []
        applicants = cls.select().where(filt == data)
        for app in applicants:
            all_data.append([app.name, app.status, app.application_number, app.city, app.email, app.school.name])
        return all_data

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
            # message = messages.greetings % (instance.name, instance.application_number, instance.school.name)
            # instance.send_email(message)

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
        # try:
        for instance in instances[:10]:
            query = SlotMentor.select().join(Mentor).switch(SlotMentor).where(Mentor.school == instance.school.name, SlotMentor.applicant >> None)
            the_list = []
            for obj in query:
                the_list.append([obj.SM_id, obj.slot, obj.mentor])
            all_data = random.choice(the_list)
            mslot1 = all_data[0]
            islot = all_data[1]
            men1 = all_data[2]
            query2 = SlotMentor.select().join(Mentor).where(Mentor.school == instance.school.name, SlotMentor.slot == islot, SlotMentor.mentor != men1, SlotMentor.applicant >> None)
            the_list2 = []
            for obj in query2:
                the_list2.append([obj.SM_id, obj.slot, obj.mentor])
            all_data2 = random.choice(the_list2)
            men2 = all_data2[2]
            mslot2 = all_data2[0]
            Interview.create(
                applicant=instance,
                slot=InterviewSlot.get(InterviewSlot.slot_id == islot.slot_id)
                )
            instance.status = "In progress"
            instance.save()
            menslot1 = SlotMentor.get(SlotMentor.SM_id == mslot1)
            menslot1.applicant = instance
            menslot1.save()
            menslot2 = SlotMentor.get(SlotMentor.SM_id == mslot2)
            menslot2.applicant = instance
            menslot2.save()
        # except:
        #     pass

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
    # def find_interview(cls, number):
    #     query = Interview.select().join(InterviewSlot).join(SlotMentor).join(Mentor).where(cls.application_number == number)
    #     print(query)
    #     data = []
    #     for i in query:
    #         print(i)
    #         data.append(Mentor.name)
    #     data.append(query.get().InterviewSlot.time)
    #     data.append(query.get().InterviewSlot.date)
    #     return data

    @classmethod
    def find_questions(cls, number):
        questions = []
        query = QuestionAnswer.select().join(cls).where(cls.application_number == number)
        for a_question in query:
            q_infos = [a_question.question, a_question.status, a_question.answer]
            questions.append(q_infos)
        return questions

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


class SlotMentor(BaseModel):

    SM_id = PrimaryKeyField()
    mentor = ForeignKeyField(Mentor)
    slot = ForeignKeyField(InterviewSlot)
    applicant = ForeignKeyField(Applicant, null=True)


class Interview(BaseModel):

    int_id = PrimaryKeyField()
    applicant = ForeignKeyField(Applicant)
    slot = ForeignKeyField(InterviewSlot)

    @classmethod
    def get_interviews(cls, filt=None, data=None):
        all_data = []
        query = (
                cls
                .select()
                .join(InterviewSlot, on=cls.slot == InterviewSlot.slot_id)
                .join(Applicant, on=cls.applicant == Applicant.basic_id))
        for all_info in query:
            data = [
                all_info.applicant.school.name,
                str(all_info.slot.date),
                str(all_info.slot.time),
                all_info.applicant.name,
                all_info.applicant.basic_id]
            app = all_info.applicant.basic_id
            obj = SlotMentor.select().join(Mentor).where(SlotMentor.applicant == app)
            for m in obj:
                data.append(m.mentor.name)
            all_data.append(data)
        return all_data


class QuestionAnswer(BaseModel):

    applicant = ForeignKeyField(Applicant)
    question = CharField()
    answer = CharField(default=None, null=True)
    status = CharField(default='New')
    mentor = ForeignKeyField(Mentor, null=True)
    date = DateField()

    @classmethod
    def filter_question(cls, filt=None, data=None):
        all_data = []
        questions = cls.select().where(filt == data)
        for question in questions:
            all_data.append([question.question, question.answer, question.status])
        return all_data
