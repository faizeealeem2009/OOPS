class Student:

    def student_details(self):
        self.name=input("Enter Name:")
        self.roll_no=int(input("Enter Roll No:"))
        self.marks =int(input("Enter Marks:"))

    def display_details(self):
        print("Student Details")
        print(f"Name:{self.name}")
        print(f"Roll No:{self.roll_no}")
        print(f"Marks:{self.marks}")


student1=Student()
student1.student_details()
student1.display_details()