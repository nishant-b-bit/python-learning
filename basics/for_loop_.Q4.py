# wap to find the factorial of the given number using a loop

n=int(input("enter the number: "))
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)    