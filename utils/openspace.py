from .table import Table, Seat
import random
import xlsxwriter


class Openspace():
    """
    """
    def __init__(self, number_of_tables=6, seats_on_table=4):
        self.number_of_tables = number_of_tables
        self.tables = []
        for table in range(number_of_tables):
            self.tables.append(Table(seats_on_table))


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
            for person in seats[0:4]:
                table.assign_seat(person)
            del seats[0:4]
    
    def display(self):
        for count, table in enumerate(self.tables, 1):
            print(f"Table {count}: {table}")
            

    def store(self, filename):
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




