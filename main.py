import csv
from utils.openspace import Openspace

people = []
with open('new_colleagues.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        people.append(line[0])

room = Openspace()
room.organize(people)
room.display()
