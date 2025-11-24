def cal_sum(a,b):
    result=a+b
    print(result)
    return result

a=cal_sum(5,10)

# why to use return
def cal_sum(a,b):
    result=a+b
    print(result)
    return result

x=cal_sum(1,5)
y=cal_sum(6,5)
total=x+y
print(total)

# when we don't use return then the value of result is not given back to us which can be used for further calculations and output of print(total) would be error 

def cal_sum(a,b):
    result=a+b
    print(result)

x=cal_sum(1,5)
y=cal_sum(6,5)
total=x+y
print(total)