class BankAccount :
    def __init__(self, initial_balance=0):
        # Initialize the account balance, defaulting to zero
         self.account_balance = initial_balance
    def deposit(self, amount):
        """Deposit specified amount ijto the account."""
        if amount > 0:  # Ensure the deposit is a positive number
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current balance: ${self.account_balance:.2f}")
