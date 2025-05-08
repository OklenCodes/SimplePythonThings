from bank_accounts import * # type: ignore

dave = BankAccount(1000, "Dave")
sarah = BankAccount(2000, "Sarah")
jim = InterestRewardsAcct(1000, "jim")
blaze = SavingsAcct(1000, "blaze")

# Perform transactions (as before)
dave.deposit(500)
sarah.withdraw(10)
dave.transfer(200, sarah)
jim.deposit(100)
blaze.withdraw(50) # Example withdrawal from savings

# View transaction history
dave.viewHistory()
sarah.viewHistory()
jim.viewHistory()
blaze.viewHistory()
