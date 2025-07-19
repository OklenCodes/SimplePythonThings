#This file is going to hold the classes of several types of bank accounts

import datetime

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        self.history = []  # Initialize an empty list for transaction history
        print(f"\nAccount '{self.name}' created.\nBalance = £{self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = £{self.balance:.2f}")

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit must be a positive amount.")
        self.balance = self.balance + amount
        self.history.append({
            "type": "deposit",
            "amount": amount,
            "timestamp": datetime.datetime.now()
        })
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
            self.history.append({
                "type":"withdraw",
                "amount": amount,
                "timestamp":datetime.datetime.now()
            })
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
            self.history.append({
                "type":"transfer_out",
                "recepient": account.name,
                "amount": amount,
                "timestamp":datetime.datetime.now()
            })
            account.history.append({
                "type": "transfer_in",
                "amount": amount,
                "recepient": self.name,
                "timestamp": datetime.datetime.now()
            })
            print('\nTranfer complete!')
            print('\n\n********')

        except BalanceException as error:
            print(f"\nTransfer interrupted!{error}")

        except BalanceException as error:
            print(f"\nTransfer history is current unavailable please try again later!{error}")

    def viewHistory(self):
        print(f"\n--- Transaction History for Account '{self.name}' ---")
        if not self.history:
            print("No Transaction recorded yet.")
            return
        for transaction in self.history:
            print(f"Type: {transaction['type']}")
            print(f"Amount: £{float(transaction['amount']):.2f}")
            print(f"Timestamp: {transaction['timestamp']}")
            if 'recipient' in transaction:
                print(f"Recipient: {transaction['recipient']}")
            if 'sender' in transaction:
                print(f"Sender: {transaction['sender']}")
            print("-" * 20)

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

        

