#create account class with 2 attributes-balance and account no. create methods for debit,credit and printing the balance
class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no 
        self.balance = balance       

    # Method to deposit money
    def credit(self, amount):
        self.balance += amount
        print(f"Amount credited: {amount}. New balance: {self.balance}")

    # Method to withdraw money
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Amount debited: {amount}. New balance: {self.balance}")

    # Method to print balance
    def show_balance(self):
        print(f"Account No: {self.account_no}, Balance: {self.balance}")

acc1 = Account(101, 5000) 
acc2=Account(233,45000)  
acc2.show_balance()
acc1.show_balance()
acc2.debit(10000)
acc1.credit(20000)

