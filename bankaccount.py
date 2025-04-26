class BankAccount:
    def __init__(self, accountNO, accountName, IFSCcode, balance):
        self.accountNO = accountNO
        self.accountName = accountName
        self.IFSCcode = IFSCcode
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
    def checkBalance(self):
        print(self.balance)


obj1 = BankAccount(123456, "head", "KLS009988", 9000)
obj1.checkBalance()
obj1.withdraw(3000)
obj1.checkBalance()
obj1.deposit(5000)
obj1.checkBalance()
obj1.withdraw(1000)
obj1.checkBalance()








