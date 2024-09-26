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
    def __init__(self):
        """
                Constructs all the necessary attributes for the seat object.

        Parameters
        ----------
            free: bool
                Is the seat free or not (default is Free)
            occupant : str
                Name of the person occupying the seat (default is "")
        """
        self.free = True
        self.occupant = ""

    def __repr__(self):
        """
        Prints if the seat is free or occupied by a person
        """
        if self.free == True:
            return f"Free seat"
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
        How many places are on the table
    seats: list
        list of seats (size = capacity)

    Methods
    -------

    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = []
        for n in range(capacity):
            seat = Seat()
            self.seats.append(seat)

    def __repr__(self):
        """
        Prints the seats on the table
        """
        return f"{self.seats}"
    
    def has_free_spot(self):
        free_spot = False
        for n in self.seats:
            if n.free == True:
                free_spot = True
        return free_spot
    
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free == True:
                seat.set_occupant(name)
                break

    def left_capacity(self):
        left_capacity = 0
        for seat in self.seats:
            if seat.free == True:
                left_capacity += 1
        return left_capacity
    





