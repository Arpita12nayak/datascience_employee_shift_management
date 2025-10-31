from employee import Employee
from exceptions import DoubleBookingError, ShiftCapacityError, EmployeeNotFound, InvalidTypeError

class ShiftEmployee:
    """
    Represents a work shift with start and end times.
    """

    def __init__(self, shift_name, capacity, start_time, end_time):
        self.shift_name = shift_name        # e.g., "Morning", "Evening"
        self.capacity = capacity            # Maximum number of employees
        self.start_time = start_time        # e.g., "09:00 AM"
        self.end_time = end_time            # e.g., "06:00 PM"
        self.employees = []                 # List of assigned employees

    def add_shift_employee(self, employee):
        if not isinstance(employee, Employee):
            raise InvalidTypeError("Only Employee objects can be assigned to a shift.")

        if employee in self.employees:
            raise DoubleBookingError(f"{employee.name} is already assigned to {self.shift_name} shift.")

        if len(self.employees) >= self.capacity:
            raise ShiftCapacityError(f"{self.shift_name} shift ({self.start_time} - {self.end_time}) is full!")

        self.employees.append(employee)

    def __str__(self):
        return (f"{self.shift_name} Shift ({self.start_time} - {self.end_time}): "
                f"{len(self.employees)}/{self.capacity} filled")


class ShiftManager:
    """
    Manages all shifts and employee assignments.
    """

    def __init__(self):
        self.shifts = {}      # {shift_name: ShiftEmployee}
        self.employees = {}   # {emp_id: Employee}
    def show_all_shifts(self):
        """
        Display all shifts and their assigned employees.
        """
        for shift in self.shifts.values():
            print(shift)  # Uses ShiftEmployee.__str__()
            for emp in shift.employees:
                print(f"   - {emp.name} ({emp.emp_id})")
    def add_employee(self, employee: Employee):
        """
        Add an employee to the system.
        """
        if not isinstance(employee, Employee):
            raise InvalidTypeError("Only Employee objects can be added.")
        self.employees[employee.emp_id] = employee

    def create_shift(self, shift_name, capacity, start_time, end_time):
        """
        Create a new shift with given name, capacity, and time range.
        """
        if shift_name in self.shifts:
            raise ValueError(f"Shift '{shift_name}' already exists.")
        self.shifts[shift_name] = ShiftEmployee(shift_name, capacity, start_time, end_time)

    def assign_employee_to_shift(self, emp_id, shift_name):
        """
        Assigns employee to a shift.
        Prevents double-booking and validates all inputs.
        """
        # Check if employee exists
        if emp_id not in self.employees:
            raise EmployeeNotFound(f"Employee with ID {emp_id} not found.")

        employee = self.employees[emp_id]

        # Check if shift exists
        if shift_name not in self.shifts:
            raise ValueError(f"Shift '{shift_name}' does not exist.")

        shift = self.shifts[shift_name]

        # Prevent double booking across all shifts
        for s in self.shifts.values():
            if employee in s.employees:
                raise DoubleBookingError(f"{employee.name} is already assigned to '{s.shift_name}' shift.")

        # Assign employee (may raise ShiftCapacityError)
        shift.add_shift_employee(employee)

    def get_employee_schedule(self, emp_id):
        """
        Return the shift(s) that the employee is assigned to.
        """
        if emp_id not in self.employees:
            raise EmployeeNotFound(f"Employee with ID {emp_id} not found.")

        employee = self.employees[emp_id]
        assigned_shifts = [s.shift_name for s in self.shifts.values() if employee in s.employees]
        return assigned_shifts if assigned_shifts else None
    
