import csv
from utils.openspace import Openspace

#Reads the lines in a csv file and convert them to a list
people = []
with open('new_colleagues.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        people.append(line[0])

#Create an Openspace object
room = Openspace()

#Put the colleagues on random tables 
room.organize(people)

#Save the table setup 
room.store('table_setup')

#Display the table setup on the screen
room.display()
