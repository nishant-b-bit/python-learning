# wap to find the sum of first n numbers using loop

n=int(input("enter the number: "))
sum=0
for i in range(1,n+1):# we wrote n+1 because we want digit up to n because range gives numbers just 1 step ahead of inital number
    sum+=i
print(sum) # initially i wrote print inside the loop that will cause the program to print every step eg when 1 is add in 0 of sum then 1 is printed, now 2 is added to 1 of sum and two is print and so on but we want to print total sum for thart we should write the print outside of the loop
