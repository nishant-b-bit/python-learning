# property


# class Student:
#     def __init__(self, phy, che):
#         self.phy = phy
#         self.che = che
#         self.percentage = str((self.phy + self.che) / 2) + "%" # here this percentage is a attrbute, calculated only once but it won't get updated when value of the subject is changed later

# st1 = Student(98, 90)
# print(st1.percentage)
# st1.che=91
# print(st1.percentage)

class Student:
    def __init__(self, phy, che):
        self.phy = phy
        self.che = che

    @property
    def percentage(self): # now percentage becomes live calcualtion(like a function) but acessed like an attribute
        return str((self.phy + self.che) / 2) + "%"

st1 = Student(98, 90)
print(st1.percentage)

st1.che = 91
print(st1.percentage)  # here even though pecentage is a function we are calling it without () like we do for the function due to property decorator
