# operators
# arithematic operators

a=10
b=20
print(a+b)
print(a*b)
print(a%b)#this is called modulo operator used to find reminder
print(a**b)# this is power operator to find a^b

#relational operators
a=40
b=20
print(a==b)#in pyhton for equal to we use double =
print(a!=b)#generally here ! means not 
print(a >=b)
print(a>b)
print(a<=b)
print(a<b) 

# assignment operators

num=10#here = is assignment operator
num+=10
print(num)
num**=10
print(num)

#logical operators

a=50
b=40
print(not False)#here not operator gives just opposite answer, here we used False boolean so output will be true
print(not True)

value1=True
value2=False
print("ans operator:",value1 and value2)#here the answer will be true only when both value1 and valu2 have True value because there is and operator 
print("ans operator:",value1 or value2)#here or operator is being used that means even if one value is only True then it will give True

# they can be used directly in expression

a=10
b=20
print("or operator:",(a==b)or(a>b))#here both the condition are False so final answer will be False