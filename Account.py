import Database


class Account:
    bank_db = Database.BankDatabase()

    def create_account(self):
        name = input("Enter your name: ")
        balance = float(input("Enter your initial deposit amount: "))
        pin_num = int(input("Enter pin num:"))
        account_number = self.bank_db.account_num()
        if 4 == len(str(pin_num)):
            self.bank_db.account[account_number] = [name.upper(), balance, str(pin_num)]
            print(f"\nSuccessful!\n"
                  f"Account number:{account_number}\n"
                  f"Name: {name}\n"
                  f"Pin Number: {pin_num}\n"
                  f"Balance :{balance}\n")
        else:
            print("Pin Number must be  4 characters in length")

    def Authentication(self, account_number, pin):
        if account_number in self.bank_db.account_list():
            acc_pin = self.bank_db.account[account_number][2]
            if pin == acc_pin:
                return True
        return False

    def getAccount(self, account_number):
        return {account_number: self.bank_db.account.get(account_number)}
