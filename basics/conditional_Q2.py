#wap to check if a number entered by the user is odd or even

num=int(input("enter the number: "))
rem=num%2#it is modulo operator that gives reminder
if(rem==0):
    print("the given number is even")
else:
    print("the give number is odd")    