class BankAccount:
    def __init__(self, IBAN, accountNo, availableFunds):
        self.iban = IBAN
        self.accNo = accountNo
        self.availableFunds = availableFunds
        self.transaction = []

    def accountinfo(self):
        print("IBAN : ", self.iban)
        print("Account Number: ", self.accNo)
        print("Available Funds: ", self.availableFunds)

    def withdraw(self):
        try:
            amount = input("How much would you like to withdraw?")
            if int(amount) > self.availableFunds:
                print("insufficient Funds")
            else:
                self.availableFunds = float(self.availableFunds) - float(amount)
                list = f"You have withdrawn{amount} and you now have {self.availableFunds}"
                self.addTransaction(list)
                print(list)
        except ValueError:
            print("Invalid Amount. Please enter a numeric value")



    def deposit(self):
        try:
            amount = input("How much would you like to deposit?")
            self.availableFunds = float(self.availableFunds) + float(amount)
            list = f"You have deposited{amount} and you now have {self.availableFunds}"
            self.addTransaction(list)
            print(list)
        except ValueError:
            print("Invalid Amount. Please enter a numeric value")

    def addTransaction(self, list):
        self.transaction.append(list)
        if len(self.transaction) > 5:
            self.transaction.pop(0)

    def show_transactions(self):
        if not self.transaction:
            print("No transactions to display.")
        else:
            print("Last 5 Transactions:")
            for t in self.transaction:
                print(f"[{t}]")


person1 = BankAccount('IE76AIBK93775783638', 123404, 50000)
print(person1.accountinfo())
person1.deposit()
person1.withdraw()
person1.show_transactions()



class MinimumBalanceAccount(BankAccount):
    def __init__(self, IBAN, accountNo, availableFunds, minimum_balance):
        """
        Initialize a MinimumBalanceAccount with additional minimum balance.
        """
        super().__init__(IBAN, accountNo, availableFunds)
        self.minimum_balance = minimum_balance

    def withdraw(self):
        """
        Overrides the withdraw method to ensure the balance doesn't go below the minimum balance.
        """
        try:
            amount = float(input("How much would you like to withdraw? "))
            if amount > self.availableFunds:
                print("Insufficient Funds")
            elif self.availableFunds - amount < self.minimum_balance:
                print(f"Cannot withdraw {amount}. Minimum balance of {self.minimum_balance} must be maintained.")
            else:
                self.availableFunds -= amount
                list = f"You have withdrawn {amount} and you now have {self.availableFunds}"
                self.addTransaction(list)
                print(list)
        except ValueError:
            print("Invalid Amount. Please enter a numeric value.")


# Example Demonstration
if __name__ == "__main__":
    # Create a MinimumBalanceAccount instance
    person2 = MinimumBalanceAccount('IE90BOFI905838382345', 567890, 5000, 1000)
    print(person2.accountinfo())

    # Perform transactions
    person2.deposit()  # User can deposit
    person2.withdraw()  # User attempts to withdraw
    person2.withdraw()  # Another withdrawal attempt
    person2.show_transactions()  # Show recent transactions
