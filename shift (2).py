from employee import Employee

# Custom exception
class ShiftCapacityError(Exception):
    """Raised when shift is full"""
    pass

class Shift_employee:
    def __init__(self, Shift_name, Capacity):
        self.Shift_name = Shift_name     # e.g., "Morning", "Evening"
        self.Capacity = Capacity         # Maximum number of employees
        self.employees = []              # list to store assigned employees

    def add_shift_employee(self, employee):
        # check if shift is full
        if len(self.employees) >= self.Capacity:
            # raise friendly error message
            raise ShiftCapacityError(
                f"Cannot assign {employee.name} to {self.Shift_name} shift: capacity {self.Capacity} reached!"
            )
        self.employees.append(employee)

    def __str__(self):
        return f"{self.Shift_name} Shift: {len(self.employees)}/{self.Capacity} filled"