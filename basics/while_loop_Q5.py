# search for a number x in the tuple

tu=(1,2,4,5,78,43,23,56)
x=int(input("enter the number: "))
i=0
while i<len(tu):
    if(tu[i]==x):
        print("found at the index: ",i)
        
    i+=1