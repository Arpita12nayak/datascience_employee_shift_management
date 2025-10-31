from employee import Employee
from shift_manager import ShiftManager
from report import Report
from exceptions import DoubleBookingError, ShiftCapacityError, EmployeeNotFoundError

def main():
    manager = ShiftManager()
    report = Report(manager)

    while True:
        print("\n--- Employee & Shift Management Menu ---")
        print("1. Add Employee")
        print("2. Create Shift")
        print("3. Assign Employee to Shift")
        print("4. View Employee Schedule")
        print("5. View Shift Summary")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            role = input("Enter Employee Role: ")
            manager.add_employee(Employee(emp_id, name, role))
            print(f"Added {name}")

        elif choice == "2":
            shift_name = input("Enter Shift Name: ")
            try:
                capacity = int(input("Enter Shift Capacity: "))
            except ValueError:
                print("Capacity must be an integer.")
                continue
            manager.create_shift(shift_name, capacity)
            print(f"Created Shift: {shift_name} with capacity {capacity}")

        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            shift_name = input("Enter Shift Name: ")
            try:
                manager.assign_employee_to_shift(emp_id, shift_name)
                print(f"Assigned Employee {emp_id} to Shift {shift_name}")
            except (DoubleBookingError, ShiftCapacityError, EmployeeNotFoundError) as e:
                print(f"Error: {e}")

        elif choice == "4":
            emp_id = input("Enter Employee ID: ")
            report.employee_schedule(emp_id)

        elif choice == "5":
            report.shift_summary()

        elif choice == "6":
            print("Exiting Employee & Shift Management...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()