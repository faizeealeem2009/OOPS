class Person:
    def __init__(self,name,city):
        self.name=name
        self.city=city

class Sports(Person):
    def __init__(self,name,city,sport_name):
        super().__init__(name,city)
        self.sport_name=sport_name

    def sportsman(self):
        print(self.name,self.city)
        print(self.sport_name)

class Academics(Person):
    def __init__(self,name,city,education,grade,**k):
        super().__init__(name,city)
        self.education=education
        self.grade=grade

class Skills(Person):
    def __init__(self,name,city,skill_set,**k):
        super().__init__(name,city,**k)
        self.skill_set=skill_set

class Employee(Skills,Academics):
    def __init__(self,name,city,education,grade,skill_set,company,designation):
        super().__init__(name=name,city=city,education=education,grade=grade,skill_set=skill_set)
        self.company=company
        self.designation=designation

    def display_employee(self):
        print(self.name,self.city)
        print(self.education,self.grade)
        print(self.skill_set)
        print(self.company,self.designation)

S1=Sports("Waseem","Malegaon","Football")
S1.sportsman()

E1=Employee("Musaddique","Malegaon","AI Making","C",["Python","Chatgpt","AI"],"OpenAI","AI Maker")
E1.display_employee()