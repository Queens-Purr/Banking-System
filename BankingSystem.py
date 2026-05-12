# Initial balance
balance = 1000

# Transaction history list
transactions = []

# Input Valdation
def validate_amount(amount):
   if amount <= 0:
      print("Invalid amount. Amount must be greater than 0.")
      return False

   return True

# Deposit money function
def deposit(amount):
    global balance
    
    if validate_amount(amount):
#User Confirmation
      confirm = input(f"Confirm deposit of ₱{amount}? (yes/no): ")
    if confirm.lower() == "yes":
        balance += amount
        transactions.append(f"Deposited: {amount}")
        print(f"Successfully deposited {amount}")
        print("New Balance: ₱{balance}")
    else:
        print("Deposit Cancelled!")

# Withdraw money function
def withdraw(amount):
    global balance

    if validate_amount(amount):
        if amount > 0 and amount <= balance:
            balance -= amount
        transactions.append(f"Withdrawn: {amount}")
        print(f"Successfully withdrew {amount}")
    else:
        print(" Warning:Insufficient balance or invalid amount")
# User Confirmation
        confirm = input(f"Confirm withdrawal of ₱{amount}? (yes/no): ")
    if confirm.lower() == "yes":
        balance -= amount
        transactions.append(f"Withdrawn: ₱{amount}")
        print(f"Successfully withdrew ₱{amount}")
        print(f"Remaining balance: ₱{balance}")

    else:
        print("Withdrawal cancelled.")
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