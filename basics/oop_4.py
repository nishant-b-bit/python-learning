# del keyword
class student:
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas

s1 = student("Nishant", 13)

print(s1.name, s1.clas)

del s1.name   # This deletes ONLY the 'name' attribute from the s1 object.

print(s1.clas)  # 'clas' will still print because it is not deleted.

print(s1.name)  # This will cause an AttributeError because 'name' no longer exists.


# del s1  # This deletes the entire object s1.
# After this, trying to use s1 will give a NameError.
