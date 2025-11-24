# some valid ways to call

def cal_sum(a=1,b=2):
    print(a+b)
    return a+b

x=cal_sum()


def cal_sum(a,b=2):
    print(a*b)
    return a+b

x=cal_sum(5)


# this is wrong 

# def cal_sum(a=5,b):
#     print(a*b)
#     return a+b

# x=cal_sum(5)
