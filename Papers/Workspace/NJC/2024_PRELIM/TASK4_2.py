# Task 4.2
class Person:
    def __init__(self, full_name, date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def is_player(self):
        return 'Maybe'
    def is_staff(self):
        return 'Maybe'

    def event_name(self):
        dob = self.date_of_birth.split('-')
        name = ''.join([i for i in self.full_name if i.isalnum()] + [str(dob[1]), str(dob[2])])

        return name

class Player(Person):
    def __init__(self, full_name, date_of_birth, team_name, char_name, score):
        super().__init__(full_name, date_of_birth)
        self.char_name = char_name
        self.team_name = team_name
        self.score = score

    def event_name(self):
        return f'{self.char_name} <{self.team_name}>'

    def is_player(self):
        return True

class Staff(Person):
    def event_name(self):
        return super().event_name() + ' Staff'

    def is_staff(self):
        return True

# Task 4.3
import csv
import sqlite3

with open('TASK4PEOPLE.CSV') as f:
    People = [i for i in csv.reader(f)]

with open('TASK4PLAYERS.CSV') as f:
    Players = [i for i in csv.reader(f)]

Event_People = []
for item in People:
    if item[2] == 'Person':
        Event_People.append(Person(item[0], item[1]))
    if item[2] == 'Staff':
        Event_People.append(Staff(item[0], item[1]))

for item in Players:
    item = [int(i) if i.isdigit() else i for i in item]
    Event_People.append(Player(*item))

# SQL
conn = sqlite3.connect('esports.db')
cursor = conn.cursor()

with conn:
    for i in Event_People:
        cursor.execute('INSERT INTO PEOPLE(FullName, DateOfBirth, IsPlayer, IsStaff) VALUES (?, ?, ?, ?)', (i.full_name, i.date_of_birth, 1 if i.is_player()==True else 0, 1 if i.is_staff()==True else 0))
        if i.is_player() == True:
            cursor.execute('SELECT PersonID FROM PEOPLE WHERE FullName = ? AND DateOfBirth = ? AND IsPlayer = ?', (i.full_name, i.date_of_birth, 1))
            ID = cursor.fetchone()[0]

            cursor.execute('INSERT INTO PLAYER VALUES (?, ?, ?, ?, ?)', (ID, i.team_name, i.char_name, i.event_name(), i.score))

    conn.commit()