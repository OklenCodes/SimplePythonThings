# SimplePythonThings

Private repo 

Simple python projects as a reminder and things to play with as a i improve python skills. 

# Basic Banking App 
[Basic Banking App](https://github.com/OklenCodes/SimplePythonThings/tree/main/SimpleBanking)- 

Project Goal
Implement security measures throughout the software development lifecycle, creating a Secure Software Development Life Cycle (SSDLC).
Automate security testing to identify vulnerabilities early in the development process, shifting security left.
Integrate security into the CI/CD pipeline for continuous security monitoring.
Ensure compliance with security best practices and industry standards.
Enable PR blocking for Critical and High Vulnerabilities.

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

Further Development
This is a basic banking system. Potential future enhancements could include:

Implementing transaction history.
Adding more account types (e.g., checking account with overdraft).
Implementing more robust error handling and input validation.
Persisting account data to a file or database.
Adding user authentication and security features.
