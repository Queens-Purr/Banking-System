# Initial balance
balance = 1000

# Transaction history list
transactions = []

# Deposit money function
def deposit(amount):
    global balance

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: {amount}")
        print(f"Successfully deposited {amount}")
    else:
        print("Invalid deposit amount")

# Withdraw money function
def withdraw(amount):
    global balance

    if amount > 0 and amount <= balance:
        balance -= amount
        transactions.append(f"Withdrawn: {amount}")
        print(f"Successfully withdrew {amount}")
    else:
        print("Insufficient balance or invalid amount")

# Check balance function
def check_balance():
    print(f"Current balance: {balance}")

# View transaction history function
def show_transactions():
    print("Transaction History:")

    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)