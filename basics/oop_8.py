# types of inheritance

# 1) Single inheritance

# Single Inheritance
class A:
    quality = "reader"

class B(A):   # B inherits from A
    color = "brown"

o1 = B()  # Object of child class B

print(o1.color)     # brown  (from B)
print(o1.quality)   # reader (inherited from A)


# 2) multi level inheritance

class Car:
    color = "red"

class Jeep(Car):     # Jeep inherits Car
    brand = "Toyota"

class Sports(Jeep):  # Sports inherits Jeep (and indirectly Car)
    type = "diesel"

o1 = Sports()

print(o1.color, o1.brand)  # red Toyota


# 3) multiple inheritance

class Student:
    name = "nishant"

class Teacher:
    name_sir = "sunil sir"

class Subject(Student, Teacher):  # inherits both
    sub = "computer system"

o1 = Subject()

print(o1.name, o1.name_sir)  # nishant sunil sir
   
           