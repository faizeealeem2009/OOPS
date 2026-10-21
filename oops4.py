class School:
    School_name="ATT High Scool"
    @classmethod
    def display_details(cls,year):
        print("This is Information.")
        cls.year=year
        print(cls.year)
        print(cls.School_name)


    def __init__(self,student_name,marks):
        self.student_name=student_name
        self.marks=marks

    def display(self):
        print(self.student_name,self.marks)
        print(self.School_name)



s1=School("Musaddiq",500)
s2=School("Farhan",600)
s3=School("Waseem",650)
# s1.display()
# s2.display()
# s3.display()
# School.School_name="MHS"
s1.display()
s2.display()
s3.display()

School.display_details(1980)