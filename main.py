ATM Machine Simulation - Console Based

Student : YagnaShri
College : KTR College of Engineering
Date    : January 15, 2026

Concepts used:
- OOP (classes for Account and ATM)
- Encapsulation (private balance and PIN)
- Custom Exceptions
- Menu-driven console interface
"""

# ---------------- Custom Exceptions ---------------- #

class InvalidPINException(Exception):
    """Raised when the user enters an incorrect PIN."""
    pass


class InsufficientBalanceException(Exception):
    """Raised when withdrawal amount exceeds available balance."""
    pass


class InvalidAmountException(Exception):
    """Raised when the entered amount is zero or negative."""
    pass


# ---------------- Account Class ---------------- #

class Account:
    """
    Simple bank account model with basic operations:
    check balance, deposit, and withdraw.
    """

    def __init__(self, account_number, holder_name, pin, opening_balance):
        self.account_number = account_number
        self.holder_name = holder_name
        # Use leading underscore to show "internal" fields (encapsulation idea)
        self._pin = pin
        self._balance = opening_balance

    def verify_pin(self, pin):
        """Return True if the given PIN matches this account."""
        return self._pin == pin

    def get_balance(self):
        """Return current account balance."""
        return self._balance

    def deposit(self, amount):
        """Increase balance by the given positive amount."""
        if amount <= 0:
            raise InvalidAmountException("Amount must be greater than zero.")
        self._balance += amount

    def withdraw(self, amount):
        """Decrease balance if sufficient funds are available."""
        if amount <= 0:
            raise InvalidAmountException("Amount must be greater than zero.")
        if amount > self._balance:
            raise InsufficientBalanceException("Insufficient balance in the account.")
        self._balance -= amount


# ---------------- ATM Class ---------------- #

class ATM:
    """ATM frontend that interacts with multiple accounts."""

    def __init__(self):
        # Pre-loaded demo accounts
        self.accounts = {
            "1001": Account("1001", "YagnaShri", "1234", 5000),
            "1002": Account("1002", "Lakshmi", "5678", 3000),
            "1003": Account("1003", "Seetha", "9999", 10000),
        }

    def start(self):
        """Entry point for ATM interaction."""
        print("\n" + "=" * 50)
        print("              KTR BANK ATM")
        print("=" * 50)
        print("\nTest Accounts for Demo:")
        print("  1001 (PIN: 1234)")
        print("  1002 (PIN: 5678)")
        print("  1003 (PIN: 9999)")
        print("=" * 50)

        account_number = input("\nEnter Account Number: ").strip()

        if account_number not in self.accounts:
            print("\n[ERROR] Account not found. Please check the number and try again.")
            return

        account = self.accounts[account_number]
        print(f"\nWelcome, {account.holder_name}!")

        # Allow up to 3 attempts for PIN
        for attempt in range(1, 4):
            pin = input(f"\nEnter PIN (Attempt {attempt}/3): ").strip()

            if account.verify_pin(pin):
                print("\nPIN verified successfully. Access granted.")
                self.show_menu(account)
                return
            else:
                remaining = 3 - attempt
                if remaining > 0:
                    print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
                else:
                    print("Too many incorrect attempts. Account temporarily locked.")

    def show_menu(self, account):
        """Display the main menu and handle user choices."""
        while True:
            print("\n" + "=" * 50)
            print("                    MENU")
            print("=" * 50)
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("=" * 50)

            choice = input("\nSelect an option (1-4): ").strip()

            if choice == "1":
                self.show_balance(account)
            elif choice == "2":
                self.handle_deposit(account)
            elif choice == "3":
                self.handle_withdrawal(account)
            elif choice == "4":
                print("\nThank you for using KTR Bank ATM. Goodbye!")
                break
            else:
                print("\nInvalid option. Please enter a number between 1 and 4.")

    def show_balance(self, account):
        """Print account details and current balance."""
        print("\n" + "-" * 50)
        print("               ACCOUNT SUMMARY")
        print("-" * 50)
        print(f"Account Number : {account.account_number}")
        print(f"Account Holder : {account.holder_name}")
        print(f"Current Balance: Rs. {account.get_balance():.2f}")
        print("-" * 50)

    def handle_deposit(self, account):
        """Ask for deposit amount and update balance."""
        try:
            amount_str = input("\nEnter deposit amount (Rs.): ").strip()
            amount = float(amount_str)
            account.deposit(amount)
            print(f"\nDeposit successful. Rs. {amount:.2f} added to your account.")
            print(f"Updated Balance: Rs. {account.get_balance():.2f}")
        except InvalidAmountException as e:
            print(f"\n[ERROR] {e}")
        except ValueError:
            print("\n[ERROR] Please enter a valid numeric amount.")
        except Exception as e:
            print(f"\n[ERROR] Unexpected error: {e}")

    def handle_withdrawal(self, account):
        """Ask for withdrawal amount and update balance if possible."""
        try:
            print(f"\nAvailable Balance: Rs. {account.get_balance():.2f}")
            amount_str = input("Enter withdrawal amount (Rs.): ").strip()
            amount = float(amount_str)
            account.withdraw(amount)
            print(f"\nWithdrawal successful. Rs. {amount:.2f} deducted from your account.")
            print(f"Remaining Balance: Rs. {account.get_balance():.2f}")
        except InvalidAmountException as e:
            print(f"\n[ERROR] {e}")
        except InsufficientBalanceException as e:
            print(f"\n[ERROR] {e}")
        except ValueError:
            print("\n[ERROR] Please enter a valid numeric amount.")
        except Exception as e:
            print(f"\n[ERROR] Unexpected error: {e}")


# ---------------- Main Program ---------------- #

if __name__ == "__main__":
    print("\n" + "*" * 50)
    print("             ATM MACHINE SIMULATION")
    print("                     By: YagnaShri")
    print("           KTR College of Engineering")
    print("*" * 50)

    try:
        atm = ATM()
        atm.start()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n[SYSTEM ERROR] {e}")

    print("\n" + "=" * 50)
    print("                  PROGRAM ENDED")
    print("=" * 50 + "\n")
```
