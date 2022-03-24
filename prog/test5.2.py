from datetime import datetime, date
class Person(object):
    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        self.nickname = surname if nickname is None else nickname
        date_format = "%d-%m-%Y"
        datetime_object = datetime.strptime(birthdate, date_format)
        self.birth_date = datetime_object.date()
 
    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return str(int(delta_in_days.days / 365.25))
 
    def get_fullname(self):
        return "{0} {1}".format(self.surname, self.first_name)

import csv
def find_oldest_person(filename):
    reader_dict = csv.DictReader(filename)
    edest_person = None
    for row_dict in reader_dict:
        surname = row_dict['surname']
        name = row_dict['name']
        birthdate = row_dict['birthdate']
        nickname = row_dict['nickname']
        person = Person(surname, name, birthdate, nickname)
        if edest_person is None or int(edest_person.get_age()) < int(person.get_age()):
            edest_person = person
    return edest_person and edest_person.get_fullname()

fp = open('people.csv')
find_oldest_person(fp)
