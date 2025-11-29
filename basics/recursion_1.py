# recursion
n=int(input("enter the number: "))

def shows(n):
    if(n==0):
        return
    print(n)
    shows(n-1)# here the function will call itself by with decreased value each time
shows(n)# this the calling that we made
