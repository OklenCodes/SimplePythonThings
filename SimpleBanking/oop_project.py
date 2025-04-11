from bank_accounts import * # type: ignore

dave = BankAccount(1000, "Dave") # type: ignore
sarah = BankAccount(2000, "Sarah") # type: ignore

dave.getBalance()
sarah.getBalance()

sarah.deposit(500)
dave.deposit(500)

dave.withdraw(20)
sarah.withdraw(10)

dave.transfer(200, sarah)
sarah.transfer(100, dave)

jim = InterestRewardsAcct(1000, "jim")

jim.getBalance()
jim.deposit(100)

jim.transfer(100, dave)

blaze = SavingsAcct(1000, "blaze")

blaze.getBalance()
blaze.deposit(100)

blaze.transfer(6000, sarah)
