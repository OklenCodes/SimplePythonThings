from bank_accounts import * #type: ignore

sam = BankAccount(1000, "sam")
dave = BankAccount(1000, "dave")
sarah = BankAccount(2000, "sarah")

sam.getBalance()
dave.getBalance()
sarah.getBalance()

dave.deposit(600)
sam.deposit(500)

sarah.withdraw(1000)
dave.withdraw(200)

#sarah.withdraw(1200) Testing Withdraw Balance exception
#dave.withdraw(1600) Testing Withdraw Balance exception

#sarah.transfer(4000, dave) #Testing Transfer Balance exception
sam.transfer(250, sarah)
dave.transfer(250, sarah)

sam.viewHistory()
sarah.viewHistory()
dave.viewHistory()

sam_ira = InterestRewardsAcct(1000, "Sam's IRA")
dave_ira = InterestRewardsAcct(1000, "Dave's IRA")

sam_ira.deposit(500)
dave_ira.deposit(500)

sam_sa = SavingsAcct(1000, "Sam's SA")
dave_sa = SavingsAcct(1000, "Dave's SA")


""""
sam_sa.withdraw(1100) # Testing Withdraw Balance Error
dave_sa.withdraw(1455) # Testing Withdraw Balance Error
"""
sam_sa.withdraw(800)
dave_sa.withdraw(455)


sam_sa.getBalance()
dave_sa.getBalance()

