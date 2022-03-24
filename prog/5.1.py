from datetime import datetime, date

class Person:
    def __init__(self, surname, first_name, birth_date, nickname = None):
        self.surname = surname
        self.first_name = first_name
        #date_format = '%d-%m-%Y'
        datetime_object = datetime.strptime (birth_date, '%Y-%m-%d') 
        self.birth_date = datetime_object.date()
        
        if nickname == None:
            self.nickname = surname
        else:
            self.nickname = nickname
    
    def get_age(self):
        now = date.today()
        delta_days = now - self.birth_date
        #print(delta_days)
        return str(int((delta_days.days) / 365.25))
        
    def get_fullname(self):
        return self.surname + ' ' + self.first_name
    

petroff = Person("Petrov", "Petro", "1952-01-02")
petroff.surname
petroff.first_name
petroff.birth_date
petroff.nickname
print(petroff.get_age())
print(petroff.get_fullname())