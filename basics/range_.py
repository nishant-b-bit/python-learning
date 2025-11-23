print(range(5)) # it will print just (0,5) because range(5) is not a list 

i=range(5)# to force the range to generate the numbers we can use this loop
for sq in i:# in this step we also can write for sq in range(5): and exclude first step
    print(sq)

#next method is

print(list(range(5)))# this will convert range into list

for i in range(4,10):# we can give start,stop,step
    print(i)

for i in range(2,10,2):
    print(i)  # output is 2,4,6,8