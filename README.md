# SimplePythonThings

Private repo 

Simple python projects as a reminder and things to play with as a i improve python skills. 


## Basic Banking  Project 

* **`oop_project.py`**: This Python file provides the output of the bank accounts and their actions/transactions 
* **`bank_accounts.py`**: This Python file defines a set of classes to represent different types of bank accounts and handle basic banking operations.
  
**Key Features:**

* **`BalanceException`**: A custom exception class raised when an account has insufficient funds for a transaction.
* **`BankAccount`**: A base class for all bank accounts, providing core functionalities:
    * **Initialization (`__init__`)**: Creates a new account with an initial balance and account name, and initializes a transaction history.
    * **Get Balance (`getBalance`)**: Displays the current balance of the account.
    * **Deposit (`deposit`)**: Increases the account balance, records the transaction, and displays the updated balance. Includes basic input validation for the deposit amount (must be a number and positive).
    * **Viable Transaction (`viableTransaction`)**: A helper method to check if the account has sufficient funds for a given transaction, raising `BalanceException` if not.
    * **Withdraw (`withdraw`)**: Decreases the account balance if sufficient funds are available (using `viableTransaction`), records the transaction, and displays the updated balance. Catches `BalanceException` if insufficient funds.
    * **Transfer (`transfer`)**: Transfers funds from the current account to another `BankAccount` instance. Checks for sufficient funds, performs the withdrawal and deposit on the respective accounts, and records the transaction in both accounts' histories. Catches `BalanceException` if insufficient funds.
    * **View History (`viewHistory`)**: Displays the transaction history for the account, including the type, amount, timestamp, and involved accounts for transfers.
* **`InterestRewardsAcct(BankAccount)`**: A subclass of `BankAccount` that provides a reward on deposits (5% interest added to the deposited amount). Overrides the `deposit` method to implement this.
* **`SavingsAcct(InterestRewardsAcct)`**: A subclass of `InterestRewardsAcct` that introduces a withdrawal fee.
    * **Initialization (`__init__`)**: Calls the parent's initialization and sets a `fee` of 5.
    * **Withdraw (`withdraw`)**: Overrides the `withdraw` method to deduct the withdrawal amount plus the `fee`. It checks if sufficient funds are available to cover both the withdrawal and the fee. Catches `BalanceException` if insufficient funds.

**Usage:**

This file is intended to be imported and used by other Python scripts to create and manage bank account objects and perform operations like depositing, withdrawing, and transferring funds. The `viewHistory` method allows tracking the transactions for each account. Custom exceptions (`BalanceException`) are used to handle cases of insufficient funds.

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
* **`guess_number.py`**: This file demonstrates the usage of the bank account classes defined in `bank_accounts.py`. It creates instances of different account types and performs various transactions.
* **`rps.py`**: This file defines the classes for different types of bank accounts: `BankAccount`, `InterestRewardsAcct`, and `SavingsAcct`, along with a custom exception `BalanceException`.

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
