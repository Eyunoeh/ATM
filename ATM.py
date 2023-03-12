import Account


class ATM:
    acc = Account.Account.bank_db

    def __init__(self, account_number):
        self.balance = self.acc.account[account_number][1]

    def withdraw(self, account_number):
        amount = float(input("Enter the amount in Cents: "))
        bal = self.balance - amount
        if bal >= 0:
            self.acc.account[account_number] = [self.acc.account[account_number][0],
                                                bal, self.acc.account[account_number][2]]
            print("Transaction successful!")
        else:
            print("Transaction Failed")

    def deposit(self, account_number):
        amount = float(input("Enter the amount in Cents: "))
        if amount > 1:
            self.acc.account[account_number] = [self.acc.account[account_number][0],
                                                self.balance + amount, self.acc.account[account_number][2]]
            print("Transaction successful!")
        else:
            print("Transaction Failed")

    def balance_inquiry(self, account_number):
        return self.acc.account[account_number][1]
