class students:
    def __init__(self, name, marks):  
        # name and marks are the parameters given when creating the object.
        # self refers to the object that is being created.
        self.name = name    # storing the name inside the object, it means in object a and b  name will be stored as name="karan" and name="rohit" respectively
        self.marks = marks  # storing the marks inside the object, it means in object a and b marks will be stored as marks=89 and marks=90 respectively

a = students("karan", 89)  # creates an object. "karan" → name, 89 → marks
print(a.name, a.marks)     # prints the data stored in object a

b = students("rohit", 90)  # creates another object with its own data
print(b.name, b.marks)
