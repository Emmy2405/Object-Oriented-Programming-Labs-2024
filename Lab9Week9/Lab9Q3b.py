#Design a class to represent a bank account. Some information you might
# want in a bank account
# are the IBAN, account number, available funds,
# a list with the last 5 transactions.
# You might also add methods to withdraw and deposit money.

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