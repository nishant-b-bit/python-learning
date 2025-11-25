# write a function to print the elements of list in a single line.(list is the parameter)
def single(element):
    print(*element)
    return element # here it is not necessary to return the vlaue to x because we are not doing any further calculations using the output
num=[1,2,3,4,56]
x=single(num) 