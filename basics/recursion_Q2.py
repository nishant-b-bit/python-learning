# write a recursive function to print all the elements in a list

def ele(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    ele(list,idx+1)
num=[1,2,34,5,32]    
ele(num)
