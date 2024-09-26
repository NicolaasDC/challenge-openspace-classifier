from table import Table
import random

class Openspace():
    """
    """
    def __init__(self, tables=[], number_of_tables=0):
        self.tables = tables
        self.number_of_tables = number_of_tables

    def __repr__(self):
        return f"{self.tables}"
    
    def organize(names):
        pass
    
    def display(self):
        return f"self.tables"

    def store(self, filename):
        pass


table_1 = Table(4)
table_2 = Table(4)
room = Openspace([table_1, table_2], 2)
print(room)