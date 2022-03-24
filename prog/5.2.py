from datetime import datetime, date
import csv

class Person:
    def __init__(self, surname, first_name, birth_date, nickname = None):
        self.surname = surname
        self.first_name = first_name
        datetime_object = datetime.strptime (birth_date, '%d.%m.%Y') 
        self.birth_date = datetime_object.date()
        
        if nickname == None:
            self.nickname = surname
        else:
            self.nickname = nickname
    
    def get_age(self):
        now = date.today()
        delta_days = now - self.birth_date
        return str(int((delta_days.days) / 365.25))
        
    def get_fullname(self):
        return self.surname + ' ' + self.first_name

fp = open('people.csv')  

def find_oldest_people(filename):
    csv_r = csv.DictReader(filename)
    oldest = 0
    for arg in csv_r:
        surname = arg['surname']
        first_name = arg['name']
        birth_date = arg['birthdate']
        nickname = arg['nickname']
        p = Person(surname,first_name,birth_date,nickname)
        age = p.get_age()
        if int(age) > oldest:
            oldest = int(age)
            name = p.get_fullname()

    return(name)
    
print(find_oldest_people(fp))