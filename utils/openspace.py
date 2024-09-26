from table import Table, Seat
import random

class Openspace():
    """
    """
    def __init__(self, tables=[]):
        self.tables = tables
        self.number_of_tables = len(self.tables)

    def __repr__(self):
        return f"{self.tables}"
    
    def organize(self, names):
        seats = []
        for name in names:
            seat = Seat()
            seat.set_occupant(name)
            seats.append(seat)
        random.shuffle(seats)
        for table in self.tables:
            while table.has_free_spot() == True:
                table.assign_seat(seats[-1])
                seats.remove[-1]


    
    def display(self):
        for table in self.tables:
            print(table)

    def store(self, filename):
        pass


table_1 = Table(4)
table_2 = Table(4)
table_3 = Table(4)
table_4 = Table(4)
room = Openspace([table_1, table_2, table_3, table_4])

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
seats = []
for name in list:
    seat = Seat()
    seat.set_occupant(name)
    seats.append(seat)
    random.shuffle(seats)
print(seats)
print(type(seats[0]))

room.organize(seats)
room.display()