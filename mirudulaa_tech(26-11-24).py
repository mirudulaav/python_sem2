#1
class BankAccount:
    def __init__(self, holder_name, account_no, balance=0):
        self.holder_name =holder_name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" Deposited: Rs{amount}.\n New balance: Rs{self.balance}")
     
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f" Withdraw: Rs{amount}.\n New balance: Rs{self.balance}")

    def check_balance(self):
        print(f"Account balance: Rs{self.balance}")

account = BankAccount("Niki", "123456789", 1000)  
account.check_balance()  
account.deposit(200)
account.withdraw(150)  
account.check_balance()

#2
class Cosmetics:
    def __init__(self, name, brand, price, category):
        self.pdt= name
        self.pbrand= brand
        self.pprice= price
        self.pcategory= category
    def display(self):
        print(f"NAME= {self.pdt}\n BRAND= {self.pbrand}\n PRICE= {self.pprice}\n CATEGORY={self.pcategory}")
cos1=Cosmetics("NYX Matte Lipstick", "NYX Professional Make up", "Rs 500", "Lipstick")
cos1.display()
cos2=Cosmetics("Couture Palette", "YSL", "Rs.600", "Eyeshadow Palette")
cos2.display()
        
        
