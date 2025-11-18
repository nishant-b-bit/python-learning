#wap to find the gratest number between 4 numbers
a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
d=int(input("enter the number: "))
if(a>=b and a>=c and a>=d):
    print(f"{a} is the greatest")
elif(b>=c and b>=d):
    print(f"{b} is the greatest")
elif(c>=d):
    print(f"{c} is the greatest")
else:
    print(f"{d} is the greatest" )           