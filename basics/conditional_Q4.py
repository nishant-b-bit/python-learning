# wap to check if a number is a multiple of 7 or not
num=int(input("enter the number: "))
result=num%7
if(result==0):
    print(f"{num} is the multiple of 7")
else:
    print(f"{num} is not the multiple of 7")