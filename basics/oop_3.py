# methods

class students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome",self.name,"whose marks is",self.marks) 
s1=students("nishant",98)
s1.welcome()           