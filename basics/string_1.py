#string
#escape sequence characters
print("my name is Nishant Budha.\nI live in Kathmandu")
print("my name is Nishant Budha.\tI live in Kathmandu")
#concatenation
name="nishant"
name2="budha"
final=(name+name2)
print(final)

#length of str

name="nishant"
name2="budha"
final=(name+name2)
print(final)
print(len(name))
print(len(name2))
print(len(final))
final2=(name+" "+name2)#here were are acutally adding two strings but also adding a space between them 
print(len(final2))#as we added space between two strings so the the total number of characters will be 13 instead of 12 because in python white sapces are also calculated as characters

#indexing

name="nishant"
print(name[3])
print(name[0])
print(name[1])

#slicing 

a="nishant"
print(a[:])#there is no starting and ending so it will think that i need whole of it and will print nishant
print(a[:6])#here ending is 6 but there is no starting so it will start from 0 and end at 6 but will include up to 5 only that is n

#string functions
# (i)endswith
str="i am nishant"
print(str.endswith("ant"))#it is used to check if the main string i.e str="i am nishant" is ending with the sub-string i.e ("ant") and print yes if it is and not if it isn't

#(ii)capitalize
print(str.capitalize())#it is used to capitalize the first character of string
"""
if we are using print(str.capitalize()) then the acual value of str is not being changed but rather a new string is created by making fist character capital i.e I 
but if we want to make changes in our original str then
str="i am nishant"
str=str.capitalize()
print(str)
"""
#(iii)replace
name="nishant budha"
print(name.replace("a","b"))#here from the string nishant budha "a" gets replaced by "b"
print(name.replace("nishant","budha"))
"""
even here the actual data is not being changed rather new string is being created and changes are made
but the actual string remain unchanged as if you print(name) then it shows same old data i.e nishant budha
"""
#(iv)find

cloth="jacket is black"
print(cloth.find("a"))#here you find that output is 1 because the very first a in whole string comes at the indexing of 1 
print(cloth.find("is"))#here you will find output is 7 because the word "is" is starting from the index 7

#(v)count
place="this is the best holiday spot"
print(place.count("i"))#it will show output 3 because there are 3 i in the string
print(place.count("the"))#it will show just 1 because there is only 1 the in string
