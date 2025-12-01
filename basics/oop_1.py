class car:  # here car is a class, or you can say a blueprint for creating objects
    color = "red"
    brand = "mercides"

a = car()  # here a is an object (instance) created based on the class car
a.color = "black"  # this sets an object property color as black for a, overriding the class property only for this object a 
print(a.color, a.brand)  # prints object's color (black) and class  brand (mercides)

b = car()  # here b is another object made using the same class car
b.brand = "hellcat"  # this sets an object property brand as hellcat for b, overriding the class property only for this object
print(b.brand, b.color)  # prints object's brand (hellcat) and class property color (red, unchanged)

print(car.color)  # this prints the class property color (red), shared by all objects unless overridden
