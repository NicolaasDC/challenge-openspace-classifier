class Seat:
    """
    A class to represent a seat

    Attributes
    ----------
    free: bool, optional
        Is the seat occupied or not (default is Free)
    occupant: str, optional
        Who is occupying the seat (default is "")

    Methods
    -------
    __str__:
        Prints if the seat is free of occupîed by someone
    set_occupant(name):
        Assign the seat to someone if it's free
    remove_occupant():
        Remove someone from the seat and return their name
    """
    def __init__(self, free=True, occupant=""):
        """
                Constructs all the necessary attributes for the seat object.

        Parameters
        ----------
            free: bool
                Is the seat free or not
            occupant : str
                Name of the person occupying the seat
        """
        self.free = free
        self.occupant = occupant

    def __repr__(self):
        """
        Prints if the seat is free or occupied by a person
        """
        if self.free == True:
            return f"The seat is free"
        if self.free == False:
            return f"{self.occupant}"

    def set_occupant(self, name):
        """
        Set the name of the occupant and change free status to False if the seat is free
        Parameter: name of the occupant
        """
        if self.free == True:
            self.occupant = name
            self.free = False
        else:
            return f"The seat is already occupied"
    
    def remove_occupant(self):
        """
        Remove the occupant from the seat and return the name of the person previously occupying the seat
        """
        previous_occupant = self.occupant
        self.occupant = ""
        self.free = True
        return previous_occupant


class Table():
    """
    A class to represent a table

    Attributes
    ----------
    capacity: int
        What is the capacity of the table
    seats: list
        list of seats (size = capacity)

    Methods
    -------

    """
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.seats = []
            
    def __repr__(self):
        if len(self.seats) == 0:
            return f"No one is at the table"
        if len(self.seats) > 0:
            return(str(self.seats))
    def has_free_spot(self):
        if len(self.seats) < self.capacity:
            return True
        else:
            return False
        
    def assign_seat(self, name):
        seat = Seat(False, name)
        self.seats.append(seat)

    def left_capacity(self):
        print(self.capacity)

seat_1 = Seat()
seat_1.set_occupant('Nicolaas')
print(seat_1)
table_1 = Table(4)
table_1.assign_seat(seat_1)
print(table_1)

            
    


             

