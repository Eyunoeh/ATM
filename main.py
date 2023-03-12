import Account
import ATM

acc = Account.Account()
while True:
    chk_account = input("do you have an account (yes or no): ").lower()
    login = False
    if chk_account == "yes":
        acc_num = input("Enter account number : ")
        pin_number = input("Enter pin number: ")

        if acc.Authentication(acc_num, pin_number):
            login = True
            session_account = acc.getAccount(acc_num)
            print(f"\n Welcome {session_account[acc_num][0]}\n")
            while login:
                atm = ATM.ATM(acc_num)
                user_choice = input("Balance inquiry [1]\n"
                                    "Deposit [2]\n"
                                    "Withdraw [3]\n"
                                    "Logout [4]\n")
                if user_choice == "1":
                    print(f"Your current balance is: {atm.balance_inquiry(account_number=acc_num)}")
                elif user_choice == "2":
                    atm.deposit(acc_num)
                elif user_choice == "3":
                    atm.withdraw(acc_num)
                elif user_choice == "4":
                    login = False

    elif chk_account == "no":
        acc.create_account()
    else:
        print("\nTry again please\n")
