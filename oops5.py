class Person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    # def dispaly_personal(self):
    #     print(self.name)
    #     print(self.gender)
    #     print(self.age)

class Student(Person):
    def __init__(self,name,gender,age,roll,marks,school):
        super().__init__(name,gender,age)
        self.roll=roll
        self.marks=marks
        self.school=school

    def display_student(self):
        print(self.name)
        print(self.roll)
        print(self.age)
        print(self.gender)
        print(self.marks)
        print(self.school)

S1=Student("Musaddique","Male",17,10,500,"ATT")
# S1.dispaly_personal()
S1.display_student()