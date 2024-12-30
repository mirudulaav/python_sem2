#3
def sum_of_digits(num):
    s= 0
    while num > 0:
        digit = num % 10
        s+=digit
        num= num// 10
    return s
n= int(input("Enter a number: "))
sum1= sum_of_digits(n)
print("The sum of the digits is:",  sum1)

#7
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid or insufficient funds for withdrawal.")
    def check_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount("123456", "John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()


