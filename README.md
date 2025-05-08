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

# Arcade

## Project Goal
To create 2 simple games then an accompanying file arcade file that joins them together. 

[Arcade](https://github.com/OklenCodes/SimplePythonThings/tree/main/Arcade)- 
The project consists of 3 file Python files:

* **`arcade.py`**: This Python script provides a simple arcade menu that allows a user to choose between two games: Rock Paper Scissors and Guess My Number.

**Key Features:**

* **Game Selection:** Presents a menu allowing the user to select which game they want to play by entering '1' for Rock Paper Scissors or '2' for Guess My Number.
* **Exit Option:** Users can exit the arcade at any time by entering 'x'.
* **Input Validation:** Basic input validation ensures the user enters a valid menu option.
* **Personalized Greeting:** Welcomes the user by name upon starting and returning to the menu.
* **Command Line Argument:** Accepts the player's name as a command-line argument for a personalized experience.

**How it Works:**

The `play_game` function manages the arcade menu loop. It greets the user and presents the game options. Based on the user's input, it either:

* Imports and runs the Rock Paper Scissors game from the `rps.py` module.
* Imports and runs the Guess My Number game from the `guess_number.py` module.
* Exits the program if the user enters 'x'.
* Prompts the user again for a valid choice if an invalid input is provided.

The script uses the `argparse` module to accept the player's name via the `-n` or `--name` command-line argument when the script is executed. This name is then used for personalized greetings throughout the arcade experience.















* **`guess_number.py`**: This file demonstrates the usage of the bank account classes defined in `bank_accounts.py`. It creates instances of different account types and performs various transactions.
* **`rps.py`**: This file defines the classes for different types of bank accounts: `BankAccount`, `InterestRewardsAcct`, and `SavingsAcct`, along with a custom exception `BalanceException`.
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
