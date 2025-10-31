class DoubleBookingError (Exception):
    """Raised When an employee is assigned to more then shift"""
    def __init__(self, message="Employee is already assigned to another shift."):
        super().__init__(message)

class ShiftCapacityError (Exception):
    """" Raised when a shift has reached its maximum capacity"""
    def __init__(self, message="Shift has reached its maximum capacity."):
        super().__init__(message)

class EmployeeNotFound (Exception):
    """" Raised when an employee is not found in records"""
    def __init__(self, message="Employee not found in records."):
        super().__init__(message)

class InvalidTypeError(Exception):
     def __init__(self, message="Invalid type provided for shift assignment."):
        super().__init__(message)