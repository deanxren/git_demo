from datetime import datetime, date
class Person(object):
    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        self.nickname = surname if nickname is None else nickname
        date_format = "%Y-%m-%d"
        datetime_object = datetime.strptime(birthdate, date_format)
        self.birth_date = datetime_object.date()
 
    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return str(int(delta_in_days.days / 365.25))
 
    def get_fullname(self):
        return "{0} {1}".format(self.surname, self.first_name)
petroff = Person("Petrov", "Petro", "1952-01-02")
