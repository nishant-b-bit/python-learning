# val=(input("enter your name: "))
# print(type(val),val)#here you are taking input as enter your name and then checking it's data type, if you enter something like nishat then it will show str but even if you enter number 2,3.4etc then again it will show integer
# so to expect integer value we use int and float to convert the input value into integer and float

#Let's write program to enter name, age and marks

name=input("enter your name: ")
age=int(input("enter your age: "))
marks=float(input("enter your marks: "))
print("welcome", name)
print("your marks is: ",marks)