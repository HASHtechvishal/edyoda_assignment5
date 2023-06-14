# Challenge 4: Implement a Banking Account

class Account():

    def __init__(self,title=None,Balance=0):
         self.title = title
         self.Balance = Balance

class SavingsAccount(Account):

    def __init__(self,interestRate):

        super().__init__()
        self.interestRate = interestRate

obj_1 = Account('Ashish', 5000)
obj_2 = SavingsAccount(5)
print(obj_1.title,obj_1.Balance)
print(obj_2.Balance,obj_2.title)





