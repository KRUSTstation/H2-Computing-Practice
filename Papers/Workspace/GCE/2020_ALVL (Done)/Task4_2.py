# YOUR ANSWER HERE
from datetime import datetime

class Person:
    def __init__(self, full_name, date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        return self.full_name
    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_date_of_birth(self):
        return self.date_of_birth
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def is_adult(self):
        dob = self.get_date_of_birth().split('-')

        return datetime.today().year - dob[0] > 18

    def screen_name(self):
        name = self.get_full_name()
        dob = self.get_date_of_birth().split('-')

        return ''.join([i for i in name if i.isalpha()]) + dob[1] + dob[2] 

class Staff(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)

    def screen_name(self):
        return super().screen_name() + "Staff"
    
    def is_adult(self):
        return True

class Student(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)
    
    def is_adult(self):
        return False
    
import csv
import sqlite3

with open('./resources/people.txt') as f:
    data = [i for i in csv.reader(f)]

people = []
for i in data:
    if i[2] == 'Person':
        people.append(Person(i[0], i[1]))
    elif i[2] == 'Staff':
        people.append(Staff(i[0], i[1]))
    elif i[2] == 'Student':
        people.append(Person(i[0], i[1]))

conn = sqlite3.connect('./school.db')
cursor = conn.cursor()
for i in people:
    cursor.execute('INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult) VALUES (?, ?, ?, ?)', (i.get_full_name(), i.get_date_of_birth(), i.screen_name(), i.is_adult() and 1 or 0))

conn.commit()
conn.close()

john = Person("John Tan", "2000-06-01")
print(john.screen_name())