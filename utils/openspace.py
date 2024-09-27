from .table import Table, Seat
import random
import xlsxwriter

class Openspace():
    """
    A class to represent an openspace office room

    Attributes
    ----------
    number_of_tables: int, optional
        How many tables are in the openspace (default is 6)
    seats_on_table: int, optional
        How many seats has each table (default is 4)

    Methods
    -------
    __repr__():
        Prints a list of tables in the open space
    organize(names):
        A list is given to the method. The method first converts the items in the list to objects of the class Seat. 
        Then shuffles the list and adds four seats to a table until the list is empty.
    display():
        
    """
    def __init__(self, number_of_tables=6, seats_on_table=4):
        """
        Constructs the openspace.

        Parameters
        ----------
            number_of_tables: int (default = 6)
                How many tables are in the openspace.
            seats_on_tables: list of seat objects (default = 4))
                How many seats are on a tables
        """
        self.number_of_tables = number_of_tables
        self.tables = []
        for table in range(number_of_tables):
            self.tables.append(Table(seats_on_table))


    def __repr__(self):
        """
        Returns a list of tables        
        """
        return f"{self.tables}"
    
    def organize(self, names):
        """
        First converts the items in a list of people to objects of the Seat class. Then assigns 4 people to a table
        """
        seats = []
        for name in names:
            seat = Seat()
            seat.set_occupant(name)
            seats.append(seat)
        random.shuffle(seats)
        for table in self.tables:
            for person in seats[0:4]:
                table.assign_seat(person)
            del seats[0:4]


    def display(self):
        """
        Prints the tables and its occupants
        """
        for count, table in enumerate(self.tables, 1):
            print(f"Table {count}: {table}")
            

    def store(self, filename):
        """
        Write the table setup to an excel file and save it
        """
        workbook = xlsxwriter.Workbook(f'{filename}.xlsx')
        worksheet = workbook.add_worksheet()
        
        row = 0
        
        for table in self.tables:
            column = 0
            worksheet.write(row, column,f"Table {row+1}")
            seats = table.seats
            for item in seats:
                column += 1
                worksheet.write(row, column, str(item))
            row += 1

        workbook.close()




