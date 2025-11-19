#wap to count the number of students with A grade in the following tuple ("a","b","a","c","a")
grade=("a","b","a","c","a")
grade=grade.count("a")# we assigned the value of grade.count("a") back in the variable grade because we discussed that tuple is immutable so it creates the new value which needs to be stored back in the variable
print(grade)
#also make the list of above values and sort from a to d
grade_list=["a","b","a","c","a"]
grade_list.sort()
print(grade_list)#so when you see output then a will be printed first, then b and finally c in ascending order
