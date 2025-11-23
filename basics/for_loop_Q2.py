# search for a number x in this tuple using loop: [1,4,5,3,2,5]

x=int(input("enter the number: "))
li=(1,4,5,3,2,5)
idx=0
for num in li:
    if num==x:
        print(f"the number {x} is found",idx)
    idx+=1    