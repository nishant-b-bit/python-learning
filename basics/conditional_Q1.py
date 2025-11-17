#Grade students based on marks
marks=int(input("enter the mark: "))# $ here initially i tried to write marks=input("enter the marks") but this is wrong because here input is string so need to make it integer to compare with other integers
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="c"
else:
    grade="D"
print("grade of the student is: ", grade)    


