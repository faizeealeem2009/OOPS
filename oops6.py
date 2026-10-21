class personal:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

class Academics:
    def __init__(self,education,marks):
        self.education=education
        self.marks=marks
        self.percent=round(sum(self.marks)/len(self.marks),2)
        if self.percent>=90:
            self.grade="A+"
        elif self.percent>=80:
            self.grade="A"
        elif self.percent>=70:
            self.grade="B"
        elif self.percent>=60:
            self.grade="C"
        elif self.percent>=50:
            self.grade="D"
        elif self.percent>=40:
            self.grade="E"
        else:
            self.grade="F"
        

class Skills:
    def __init__(self,skill_set):
        self.skill_set=skill_set

class Employee(personal,Academics,Skills):
    def __init__(self,name,gender,education,marks,skill_set,empid,dept,company,salary):
        personal.__init__(self,name,gender)
        Academics.__init__(self,education,marks)
        Skills.__init__(self,skill_set)
        self.empid=empid
        self.dept=dept
        self.company=company
        self.salary=salary
        self.gross=self.salary*12

        if self.grade=="A+":
            self.gross+=70000
        elif self.grade=="A":
            self.gross+=60000
        elif self.grade=="B":
            self.gross+=50000
        elif self.grade=="C":
            self.gross+=40000
        elif self.grade=="D":
            self.gross+=30000
        elif self.grade=="E":
            self.gross+=20000
        else:
            self.gross+=5000

    def display_empdata(self):
        print(self.name,self.gender,self.education,self.skill_set,self.empid,self.dept,self.company,self.grade,self.gross,sep="\n")




E1=Employee("Musaddique420","Male","11th",[50,60,70,80,90,75],["Python","Harami Chale"],420,"Programming","ABCDE",50000)
E1.display_empdata()