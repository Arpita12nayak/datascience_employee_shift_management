from employee import Employee
from shift import Shift
from exceptions import DoubleBookingError, ShiftCapacityError, EmployeeNotFoundError

class ShiftManager:
    """
    Manages all shifts and employee assignments.
    """

    def __init__(self):
        # HINT: Store shifts in a dictionary {shift_name: Shift}
        #       Store employees in a dictionary {emp_id: Employee}
        pass  

    def add_employee(self, employee: Employee):
        """
        Add an employee to the system.
        """
        pass  

    def create_shift(self, shift_name, capacity):
        """
        Create a new shift with given name and capacity.
        """
        pass  

    def assign_employee_to_shift(self, emp_id, shift_name):
        """
        Assigns employee to a shift.
        HINT: Prevent double-booking (employee already in another shift).
        HINT: Raise errors from exceptions.py if invalid.
        """
        pass  

    def get_employee_schedule(self, emp_id):
        """
        Return the shift(s) that the employee is assigned to.
        """
        pass  
