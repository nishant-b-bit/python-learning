# inheritene 
 
class car:
  color="black"
class toyotacar(car):
    def __init__(self,name):
        self.name=name
car1=toyotacar("fortuner") # this car1 is the object of class toyotacar which is inheriting the attributes of parent class
print(car1.color)# here python will look for color in object car1 but there is no color in object car1 there is only name so now it will check the inherited 
# attribute for color and then it will print black
# that means python prefers instance attribute over class, if there was already a attribut called color in object then it would print it instead of black        

