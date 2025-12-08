# static methodc
class calculation:
    @staticmethod 
    def add(a,b): 
        total=a+b
        return total # return will send you the value where you called it 
print(calculation.add(2,3))    
# here we don't have object attribute but deu to staticmethod it worked