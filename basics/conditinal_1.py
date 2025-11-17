# conditional statements

light="pink"
if(light=="red"):
    print=("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")#else is only used once and at last and program only comes to this point when all the above condition are flase

"""
here this program is like, at first if will check whether light is red or not if it is red then at the same 
time program will print stop and program will not move any further but as the value of light is green so it will move to 
elif and it will check whether the colour of light is yellow if it is then it will print look otherwise program will move to next 
elif and it will check whether the value of light is green and if it is then it will print go.

so, main difference between "if" and "elif" is that if checks the condition all the time but 
elif only checks the conditon when it is not true during if 

num=10
if(num>2):
    print("greater than 2)
if(num>4):
    print("greater than 4)

here you will get two output that greater than 2 and 4, so it means if checks the condition all the times but
num=10
if(num>2):
    print("greater than 2)
elif(num>4):
    print("greater than 4)

now in this case only greater than 2 will be printed because if condition is right so program won't
got to next step
"""
#nesting
"""
First checks if age >= 18

If true, you enter the first block:

Then checks if age >= 80

If true → prints "not able to drive"

Else → prints "can drive"

If age < 18 → prints "cannot drive"
"""
age=int(input("enter age: "))
if(age>=18):
    if(age>=80):
        print("not able to drive")
    else: 
        print("can drive") 
else:
    print("cannot drive")              
