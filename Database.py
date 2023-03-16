import random


class BankDatabase:
    account = {}

    def account_list(self):
        return list(self.account.keys())

    def account_num(self):
        while True:
            rand_num = random.randint(000000, 999999)
            if rand_num not in self.account_list():
                return str(rand_num)
