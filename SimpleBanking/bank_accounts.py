#This file is going to hold the classes of several types of bank accounts

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = £{self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = £{self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
            f"\nSorry, account '{self.name}' has insufficient balance to perform this transaction")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print ("Withdraw Complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error} ")


    def transfer(self, amount, account):
        try:
            print("\n********\n\nTranferring funds********")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTranfer complete!')
            print('\n\n********')

        except BalanceException as error:
            print(f"\nTransfer interrupted!{error}")



class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05) 
        print("\nDeposit complete")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialamount, acctname):
        super().__init__(initialamount, acctname)  
        self.fee = 5

    def withdraw(self, amount):
        try: 
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount  + self.fee)
            print("\nWithdraw Complete")

        except BalanceException as error:
            print(f"\nWithdraw Interrupted:{error}")

        

