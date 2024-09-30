# challenge-openspace-classifier
Our company moved to a new office space. This is a program that runs everyday to re-assign everybody to a new seat.

# Repo structure
.
├── src/
│   ├── openspace.py
│   ├── table.py
│   └── utils.py
├── .gitignore
├── main.py
├── new_colleagues.csv
├── table_setup.xlsx
└── README.md

# Usage
Clone the repository to your local machine.

2 .To run the script, you can execute the main.py file from your command line:

```
python main.py
```

The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "table_setup.xslx" file in your root directory.

input_filepath = "new_colleagues.csv"
output_filename = "table_setup.xslx"

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

# Timeline
This project took two days for completion.

# Personal Situation
This project was done as part of the AI Boocamp at BeCode.org.

Connect with me on LinkedIn.