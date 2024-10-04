class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN")
            return False

    def balance_inquiry(self):
        if self.check_pin():
            print(f"Your current balance is: {self.balance}")
            self.transaction_history.append("Balance inquiry")

    def cash_withdrawal(self, amount):
        if self.check_pin():
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful! New balance is: {self.balance}")
                self.transaction_history.append(f"Withdrew {amount}")
            else:
                print("Insufficient balance!")

    def cash_deposit(self, amount):
        if self.check_pin():
            self.balance += amount
            print(f"Deposit successful! New balance is: {self.balance}")
            self.transaction_history.append(f"Deposited {amount}")

    def pin_change(self):
        if self.check_pin():
            new_pin = input("Enter new PIN: ")
            self.pin = new_pin
            print("PIN successfully changed")
            self.transaction_history.append("PIN changed")

    def show_transaction_history(self):
        if self.check_pin():
            if self.transaction_history:
                print("Transaction History:")
                for transaction in self.transaction_history:
                    print(transaction)
            else:
                print("No transactions found!")

# Simulating ATM operations
atm = ATM(1000)  # initial balance set to 1000

while True:
    print("\n1. Balance Inquiry\n2. Cash Withdrawal\n3. Cash Deposit\n4. PIN Change\n5. Transaction History\n6. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        atm.balance_inquiry()
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        atm.cash_withdrawal(amount)
    elif choice == 3:
        amount = float(input("Enter amount to deposit: "))
        atm.cash_deposit(amount)
    elif choice == 4:
        atm.pin_change()
    elif choice == 5:
        atm.show_transaction_history()
    elif choice == 6:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
