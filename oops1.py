class Employees:
    def __init__(self):
        self.emp_id=int(input("Enter Emp_id:"))
        self.emp_name=input("Enter Name:")
        self.department=input("Enter Department:")
        self.designation=input("Enter Designation:")
        self.salary=int(input("Enter Salary:"))
        self.city=input("Enter City:")
    def calculate_salary(self):
        self.gross_salary=self.salary*12
    def display(self):
        print("Employee Data")
        print(f"Employee Name:{self.emp_name}")
        print(f"Employee Id:{self.emp_id}")
        print(f"EMployee Department:{self.department}")
        print(f"EMployee Designation:{self.designation}")
        print(f"Employee Salary:{self.salary}")
        print(f"Employee Actual Salary:{self.gross_salary}")
        print(f"Employee City:{self.city}")

E1=Employees()
E1.calculate_salary()
E1.display()