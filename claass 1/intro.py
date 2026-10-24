class BankAccount:
    def __init__(self, account_number, account_holdername, balance):
        self.account_number= account_number
        self.account_holdername= account_holdername
        self.balance=balance
    def deposit(self):
        amount= int(input("Enter the amount you want to deposit into your account: "))
        if amount > 0:
            self.balance= self.balance + amount
            print("Amount deposited")
        else:
            print("Thank You")