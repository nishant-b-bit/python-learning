# WAF to take input of a number and print string odd if it odd and print even if it is even

num=int(input("enter the number: "))
def check(wor):
    if wor%2==0:
        print("even")
        # for returning the value to "a" we can write return "even" here
    
    else:
        print("odd") 
        # for returning the vlaue only when if condition is false then write return "odd" to "a"

a=check(num) # it is not compulsory to assign the variable a but if you want to use the output for further steps then it is necessary because return will return th value in it   

