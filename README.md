# SimplePythonThings

Private repo 

Simple python projects as a reminder and things to play with as a i improve python skills. 

SimpleBanking - 
The project consists of two main Python files:
* **`oop_project.py`**: This file demonstrates the usage of the bank account classes defined in `bank_accounts.py`. It creates instances of different account types and performs various transactions.
* **`bank_accounts.py`**: This file defines the classes for different types of bank accounts: `BankAccount`, `InterestRewardsAcct`, and `SavingsAcct`, along with a custom exception `BalanceException`.
The oop_project.py script demonstrates the following actions:
Creating Accounts: Creates instances of BankAccount for "Dave" and "Sarah" with initial balances.
Checking Balances: Calls the getBalance() method to display the initial balances.
Deposits: Performs deposit transactions into both Dave's and Sarah's accounts.
Withdrawals: Performs withdrawal transactions from both Dave's and Sarah's accounts.
Transfers: Transfers funds between Dave's and Sarah's accounts.
Interest Rewards Account: Creates an instance of InterestRewardsAcct for "jim," performs a deposit (which includes an interest reward), and transfers funds to Dave's account.
Savings Account: Creates an instance of SavingsAcct for "blaze," performs a deposit, and attempts a large transfer (which will likely fail due to insufficient funds after the withdrawal fee is applied).
