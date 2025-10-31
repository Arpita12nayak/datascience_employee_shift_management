from employee import Employee
from shift import Shift
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
            # HINT: Ask for employee details and create Employee object
            pass  

        elif choice == "2":
            # HINT: Ask for shift_name and capacity, then create Shift
            pass  

        elif choice == "3":
            # HINT: Ask for emp_id and shift_name, then assign employee
            pass  

        elif choice == "4":
            # HINT: Fetch schedule of a specific employee
            pass  

        elif choice == "5":
            # HINT: Show shift-wise summary report
            pass  

        elif choice == "6":
            print("Exiting Employee & Shift Management...")
            break  

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
