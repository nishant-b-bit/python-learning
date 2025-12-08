# class method
class student:
    name="sameer"
    @classmethod
    def newname(cls,name):
        cls.name=name
o1=student()
o1.newname("nishant")
print(o1.name)
print(student.name)


