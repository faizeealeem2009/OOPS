class Employee:
    def __init__(self,empid,empname,company):
        self.empid=empid
        self.empname=empname
        self.company=company

    def display(self):
        print(self.empid,self.empname,self.company)

class Sales(Employee):
    def __init__(self,empid,empname,company,profile,team):
        super().__init__(empid,empname,company)
        self.profile=profile
        self.team=team

    def display_sales(self):
        self.display()
        print(self.profile,self.team)

class HR(Employee):
    def __init__(self,empid,empname,company,management_level):
        super().__init__(empid,empname,company)
        self.management_level=management_level
    
    def display_HR(self):
        self.display()
        print(self.management_level)

class Development(Employee):
    def __init__(self,empid,empname,company,skills,project):
        super().__init__(empid,empname,company)
        self.skills=skills
        self.project=project

    def display_dev(self):
        self.display()
        print(self.skills,self.project)


S1=Sales(102,"Musaddique","AI","AI Maker","AI")
H1=HR(104,"Farhan","Infosys","HR Manager")
D1=Development(106,"Waseem","Google",["Python","SQL"],"Exam Software")

S1.display_sales()
H1.display_HR()
D1.display_dev()