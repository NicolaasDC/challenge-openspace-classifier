import sys
import os
import csv

sys.path.append(os.path.abspath("openspace-organizer/utils"))

from table import *
from openspace import *


people = []
with open('new_colleagues.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        people.append(line[0])

room = Openspace()
room.organize(people)
room.display()
