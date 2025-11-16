#type conversion

a=2
b=4.25
print(a+b)#here a is integer and b is float but what interpreter does is convert integer to float because float is superior to integer so it make 2 at 2.0 now both are float so answer will be 6.25 a float

#type casting

# a="2"
# b=3
# print(a+b)here program will crash because we are trying to add integer and string

a=int("2")
b=3
print=(a+b)#now we will get answer 6.25 because string has been converted into integer

#but note that
# a=int("nishant")this is not going to be converted into integer because they are letters not numbers
# b=3
"""
but number can be converted into string

"""
