#wap to find the greatest of 3 numbers entered by the user

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
if(a>=b and a>=c):
    print(f"{a} is the greatest")
elif(b>=c):
    print(f"{b} is the greatest",) 
else:
    print(f"{c} is the greatest",)       