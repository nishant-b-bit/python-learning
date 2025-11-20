# wap to enter the marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and add the keys and their values one by one. Use subjects as keys amnd marks as values

marks={}
s1=int(input("enter the marks of science: "))
marks.update({"science":s1})
s2=int(input("enter the marks of computer: "))
marks.update({"computer":s2})
s3=int(input("enter the marks of maths: "))
marks.update({"maths":s3})
print(marks)