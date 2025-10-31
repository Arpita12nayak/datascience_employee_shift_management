from employee import Employee
from shift import Shift_employee, ShiftCapacityError
from shift_manager import ShiftEmployee,ShiftManager
def main():
    print("Employee & Shift Management System\n")

    # Create employees
    e1 = Employee(101, "Alice", "Manager")
    e2 = Employee(102, "Bob", "Developer")
    e3 = Employee(103, "Charlie", "Analyst")
    e4 = Employee(104, "Deck", "Software Engineering")
    e5 = Employee(105, "Dev", "HR")

    # Show all employees
    print("All Employees:")
    Employee.show_all()
    print("\n")

    # Create shifts
    morning_shift = Shift_employee("Morning", 2)
    evening_shift = Shift_employee("Evening", 2)

    # Assign employees to Morning shift
    for emp in [e1, e2, e3]:
        try:
            morning_shift.add_shift_employee(emp)
        except ShiftCapacityError as e:
            print(f"⚠️ {e}")

    # Assign employees to Evening shift
    for emp in [e4, e5]:
        try:
            evening_shift.add_shift_employee(emp)
        except ShiftCapacityError as e:
            print(f"⚠️ {e}")

    # Show shift info
    print("\nShifts Info:")
    print(morning_shift)
    print(evening_shift)

if __name__ == "__main__":
    

    # Create manager
    manager = ShiftManager()

    # Add employees
    e1 = Employee(1, "Alice", "Managerr")
    e2 = Employee(2, "Bob", "Developer")
    e3 = Employee(3, "Charlie", "Analyst")
    e4 = Employee(4,"Deck","Software Engineering")

    manager.add_employee(e1)
    manager.add_employee(e2)
    manager.add_employee(e3)
    manager.add_employee(e4)

    # Create shifts
    manager.create_shift("Morning", 2, "09:00 AM", "06:00 PM")
    manager.create_shift("Evening", 2, "06:00 PM", "09:00 PM")

    # Assign employees
    manager.assign_employee_to_shift(1, "Morning")
    manager.assign_employee_to_shift(2, "Morning")
    manager.assign_employee_to_shift(3, "Evening")
    manager.assign_employee_to_shift(4, "Evening")

    # Show schedules
    print(manager.get_employee_schedule(1))  # ['Morning']
    print(manager.get_employee_schedule(2))  # ['Morning']
    print(manager.get_employee_schedule(3))  # ['Evening']
    print(manager.get_employee_schedule(4))  # ['Evening']

    # Show all shifts with employees
    manager.show_all_shifts()
