# SimplePythonThings

Private repo 

Simple python projects as a reminder and things to play with as a i improve python skills. 

# Basic Banking App 

## Project Goal
To create a simple banking system in python that becomes more intricate over time using different modules and functions to mimic a real banking system.

[Basic Banking App](https://github.com/OklenCodes/SimplePythonThings/tree/main/SimpleBanking)- 
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
history List: An empty list self.history is created when a BankAccount object is initialized.

Recording Transactions:
In deposit, withdraw, and transfer, a dictionary containing details of the transaction (type, amount, timestamp) is created and appended to the self.history list.
For transfers, both the sending and receiving accounts record the transaction, noting the other party involved.
viewHistory() Method: This new method iterates through the self.history list and prints the details of each transaction in a readable format.

Implementing robust error handling:
Including type error and value error if statements to ensure that the values transferred or deposited are positive or above 0. More indepth error handling can include - IOError, ConnectionError if i am connecting to API's or Databases.
InvalidAccountError for when an invalid account object is passed.
TransactionFailedError for general transaction failures not due to insufficient balance.
Returning Error Codes or Status Objects that the calling code can then use to handle errors in a more programmatic way. This makes the could make the code more reusable and testable.



## Further Development
Potential future enhancements could include:

* ~Implementing transaction history.~
* ~Implementing more robust error handling and input validation.~
* Persisting account data to a file or database.
* Adding user authentication and security features.
