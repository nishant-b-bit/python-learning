# Public attribute example
class person:
    name = "nishant"

o1 = person()
print(o1.name)  
# Output: nishant
# Here we can access the attribute directly from outside the class because it is public.

# Sometimes, for security or encapsulation purposes, we want to prevent direct access to attributes from outside.
# We can make attributes private by adding two underscores __ in front of their name.

# Private attribute example
class person: 
    def __init__(self, name):
        self.__name = name   # Private attribute

    def nameee(self):
        print(self.__name)   # Accessing private attribute from inside the class works fine

o1 = person("nishant")
o1.nameee()  
# Output: nishant
# The private attribute __name can be accessed from inside the class using a method like this.

print(o1.__name)  
# This will raise an AttributeError because __name is private and cannot be accessed directly from outside.


# Summary:
# - Public attributes: accessible anywhere.
# - Private attributes (__attribute): accessible only inside the class (or via methods/properties).

