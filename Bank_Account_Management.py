import random
import sys 
class BANK():

    def __init__(self, name, account_number, balance =0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def create_account(self):
        print("\n DETAILS OF ACCOUNT")
        print(f"Names: {self.name.capitalize()}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
    
    def check_balance(self):
        print(f"Balance: {self.balance}")
        print()
        
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insuficient Balance")
            print(f"Balance: is {self.balance}")
            print("Try again, Insuficient Balance")
            print()
        elif self.balance - self.amount == 0 or self.balance - self.amount < 500:
            print("Your account can't remain Less than 500")
            print(f"Balance: is {self.balance}")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"{self.amount} Withdrawn Successfully")
            print(f"Your New balance is {self.balance}")
            print()
            
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.amount + self.balance
        print("Transaction Completed Successfully")
        print(f"Your new Balance is {self.balance}")
        print()
            
    def transaction(self):
        print("""
                TRANSACTIONS
            ...................
                   MENU:
            ...................
                1.ACCOUNT DETAILS
                2.WITHDRAW
                3.CHECK BALANCE
                4.DEPOSIT
                5.EXIT
            .......................
            """)
        while True:
            try:
                a = int(input("Choose 1, 2, 3,4 or 5. To Perform Transaction:"))
            except:
                print("Try Again, Choose  between (1, 2, 3,4 or 5) only\n")
                continue
            else:
                if a == 1:
                    bank.create_account()
                elif a == 2:
                    amount = int(input("Enter Amount To Withdraw: "))
                    bank.withdraw(amount)
                elif a == 3:
                    bank.check_balance()
                elif a == 4:
                    amount = int(input("Enter Amount To Deposit:"))
                    bank.deposit(amount)
                elif a == 5:
                    print(f"""
                          Completed
                          Transaction Number: {random.randint(1000,5000)}
                          Names: {self.name.upper()}
                          Account Number: {self.account_number}
                          Balance: {self.balance}
                               Thank you for Choosing us
                          ...................................
                          """)
                    sys.exit()
print("  \n =========== WELCOME TO OUR Simple Bank Account System ===========")
print("     #################################################################")
print("\n\n =========== CREATE ACCOUNT  HERE ===========")
name = input("\n Please enter Full Names:")
account_number = input("Enter Account Number:")
print("=========== Welcome, Account have been successfully created ===========\n")
bank = BANK(name, account_number)

while True:
    options = input("Type (Y/y) if you want to Continue Transaction or (N/n) to Stop(Exit):")
    
    if options.upper() == "Y".upper():
        bank.transaction()
    elif options.upper() == "N".upper():
        print("=========== Thank you for Choosing us ===========")
        break
    else:
        print("Try again!")
        print("Type (Y/y) if you want to Continue Transaction or (N/n) to Stop(Exit): ")