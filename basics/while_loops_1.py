#while loop (python will check the condition and print the value until and unless condition becomes false)


#while True: #here condition is true so true is always true it can't be false Nishant will be printed infinite times and it won't stop
    #print("nishant")
i=1
while i<=20:
    print("Nishant")
    #if we try to print just like this then Nishant will be printed only one time because we assigned i=1 and on second step condition will be checked and as it is true so Nishant will be printed but loop will not repeat it self so we need to increase the value of i by 1 and loop will repeat again
    i+=1#here at first condition will be checked when value of i is 1 then nishant will be printed then value of i will be increased by 1 i.e it becomes 2 so again condition will be checked and nishant will be printed untill the value of i becomes 21 which makes the condition false 

num=1 # this variable is called iterator in loop and the process of repetation of loop is called iteration
while num<10:
    print("hello",num)# by printing num as well we will be able to see how many times hello is being printed
    num+=1

# Break

n=6
while 5<n<10: 
    print(n)
    if n==9:
        break
    n+=1
    
# continue

i=1
while i<=5:
    if(i==4):
        i+=1
        continue
    i+=1
    print(i)  