class Shift:
    """
    Represents a work shift (morning/evening/night).

    Attributes:
        shift_name (str): Name of the shift.
        capacity (int): Maximum number of employees allowed.
        employees (list): Employees assigned to this shift.
    """

    def __init__(self, shift_name, capacity):
        # HINT: Initialize employees as an empty list
        pass  

    def assign_employee(self, employee):
        """
        Assigns an employee to the shift.
        HINT: Check if capacity is not exceeded before assigning.
        """
        pass  

    def __str__(self):
        """
        Returns a readable summary:
        "Shift: Morning | Capacity: 3 | Employees: [Alice, Bob]"
        """
        pass  
