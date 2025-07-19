from bank_accounts import * # type: ignore

sam = BankAccount(1000, "sam")
dave = BankAccount(1000, "Dave")
sarah = BankAccount(2000, "Sarah")


sarah.getBalance()
sam.getBalance()
dave.getBalance()


# Perform transactions (as before)
dave.deposit(500)
sam.deposit(100)
#Want to check if error works?

sarah.withdraw(1000)
dave.withdraw(400)
#Want to check if error works?

sam.transfer(250, sarah)
sarah.transfer(150, dave)
#Want to check if error works?


# View transaction history
dave.viewHistory()
sarah.viewHistory()
sam.viewHistory()

sam_ira = InterestRewardsAcct(1000, "Sam's IRA")
dave_ira = InterestRewardsAcct(1000, "Dave's IRA")


sam_ira.deposit(500) 
dave_ira.deposit(300) 

sam_sa = SavingsAcct(1000, "Sam's SA")
dave_sa = SavingsAcct(1000, "Dave's SA")

sam_sa.withdraw(800)
dave_sa.withdraw(455)
#Want to try withdraw error?

sam_sa.getBalance()
dave_sa.getBalance()
