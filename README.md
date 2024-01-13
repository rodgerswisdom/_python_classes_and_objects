
---

# Bank Account Project

## Overview

The Bank Account Project is a Python program that implements a simple bank account using object-oriented programming principles. It includes a `BankAccount` class with methods for initializing the account, depositing money, withdrawing money, and checking the account balance.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Object-oriented design with a `BankAccount` class.
- Initialization of an account with the account holder's name and an optional initial balance.
- Deposit method to add funds to the account.
- Withdraw method to subtract funds from the account (with a check for insufficient funds).
- Get Balance method to retrieve the current account balance.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rodgerswisdom/_python_classes_and_objects.git
   cd _python_classes_and_objects
   ```

2. Run the Python script:

   ```bash
   python bank_account.py
   ```

## Usage

The `BankAccount` class provides the following methods:

- `__init__(self, account_holder, total_balance=0)`: Initializes the account with the account holder's name and an optional initial balance.

- `deposit(self, amount)`: Adds a specified amount to the account balance.

- `withdraw(self, amount)`: Subtracts a specified amount from the account balance, checking for insufficient funds.

- `get_balance(self)`: Returns the current balance of the account.

## Example

```python
# Create an instance of the BankAccount class
Person1 = Bank_account("John Doe")

# Perform transactions
Person1.deposit(500)
Person1.deposit(1500)
Person1.deposit(46)
Person1.withdraw(250)
Person1.get_balance()
```

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) if you'd like to contribute to the project.



---


