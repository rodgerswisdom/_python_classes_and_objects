

---

# Bank Account Project

## Overview

The Bank Account Project is a simple Python program that demonstrates the implementation of a basic bank account using object-oriented programming principles. It includes a `BankAccount` class with methods for initializing the account, depositing money, withdrawing money, and checking the account balance.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Object-oriented design with a `BankAccount` class.
- Initialization of account with account holder's name, initial balance, and total balance.
- Deposit method to add funds to the account.
- Withdraw method to subtract funds from the account (with a check for insufficient funds).
- Get Balance method to retrieve the current account balance.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/bank-account-project.git
   cd bank-account-project
   ```

2. Run the Python script:

   ```bash
   python main.py
   ```

## Usage

The `BankAccount` class provides the following methods:

- `__init__(self, account_holder, initial_balance, total_balance)`: Initializes the account with the account holder's name, initial balance, and total balance.

- `deposit(self, amount)`: Adds a specified amount to the account balance.

- `withdraw(self, amount)`: Subtracts a specified amount from the account balance, checking for insufficient funds.

- `get_balance(self)`: Returns the current balance of the account.

## Example

```python
# Create an instance of the BankAccount class
account = BankAccount("John Doe", 1000.0, 1000.0)

# Perform transactions
account.deposit(500.0)
account.withdraw(200.0)

# Get and print the final balance
print("Final Balance:", account.get_balance())
```

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) if you'd like to contribute to the project.



---

