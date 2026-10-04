"""
Bank Account Management System
--------------------------------
A small OOP project demonstrating:
- Encapsulation (private balance attribute)
- Inheritance (SavingsAccount, CurrentAccount extend Account)
- Polymorphism (overridden withdraw() method)
- A menu-driven interface for user interaction
"""


class Account:
    """Base class representing a generic bank account."""

    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.__balance = balance  # private attribute (encapsulation)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print(f"Account No: {self.account_number}")
        print(f"Holder Name: {self.account_holder_name}")
        print(f"Balance: {self.__balance}")


class SavingsAccount(Account):
    """Savings account with an interest rate."""

    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest added: {interest}")

    def display_info(self):
        super().display_info()
        print(f"Account Type: Savings (Interest Rate: {self.interest_rate}%)")


class CurrentAccount(Account):
    """Current account with an overdraft limit (allows negative balance up to limit)."""

    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Overriding withdraw to allow overdraft (polymorphism)
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        available = self.get_balance() + self.overdraft_limit
        if amount > available:
            print("Withdrawal exceeds overdraft limit.")
            return
        # Access balance via parent's deposit with negative amount trick avoided;
        # instead directly reduce using parent methods
        new_balance = self.get_balance() - amount
        # Use deposit/withdraw of base carefully: simplest is to call super() logic manually
        self._apply_withdrawal(amount)

    def _apply_withdrawal(self, amount):
        # Helper to bypass base class's insufficient funds check
        # by directly manipulating balance through deposit (negative not allowed),
        # so we recreate the logic here using the public getter and a protected setter pattern.
        current = self.get_balance()
        self.__dict__['_Account__balance'] = current - amount
        print(f"Withdrew {amount}. New balance: {self.get_balance()}")

    def display_info(self):
        super().display_info()
        print(f"Account Type: Current (Overdraft Limit: {self.overdraft_limit})")


class Bank:
    """Manages a collection of accounts."""

    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def total_deposits(self):
        return sum(acc.get_balance() for acc in self.accounts.values())

    def list_accounts(self):
        if not self.accounts:
            print("No accounts yet.")
            return
        for acc in self.accounts.values():
            acc.display_info()
            print("-" * 30)


def get_float_input(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def create_account():
    acc_num = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = get_float_input("Enter initial deposit: ")

    acc_type = input("Account type (savings/current): ").strip().lower()

    if acc_type == "savings":
        rate = get_float_input("Enter interest rate (%): ")
        return SavingsAccount(acc_num, name, balance, rate)
    else:
        limit = get_float_input("Enter overdraft limit: ")
        return CurrentAccount(acc_num, name, balance, limit)


def main():
    bank = Bank()

    menu = """
--- Bank Menu ---
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Add Interest (Savings only)
6. List All Accounts
7. Total Bank Deposits
8. Exit
"""

    while True:
        print(menu)
        choice = input("Enter choice: ").strip()

        if choice == "1":
            account = create_account()
            bank.add_account(account)
            print("Account created successfully!")

        elif choice == "2":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                amount = get_float_input("Enter deposit amount: ")
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                amount = get_float_input("Enter withdrawal amount: ")
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                print(f"Balance: {account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "5":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account and isinstance(account, SavingsAccount):
                account.add_interest()
            else:
                print("Not a valid savings account.")

        elif choice == "6":
            bank.list_accounts()

        elif choice == "7":
            print(f"Total Bank Deposits: {bank.total_deposits()}")

        elif choice == "8":
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()