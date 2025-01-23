class BankAccount: 
    def __init__(self,account_number,balance): 
                  self.__account_number=account_number 
                  self.__balance=balance 
    def check_account_number(self): 
                  print("Your account number is:",self.__account_number) 
    def deposit(self): 
                 deposit=int(input("Enter your deposit amount:")) 
                 self.__balance+=deposit 
                 print("You deposited successfully") 
    def withdraw(self): 
                 withdraw=int(input("Enter the withdraw amount:")) 
                 if self.__balance>withdraw: 
                          self.__balance-=withdraw 
                          print("you have withrawn successfully") 
                  else: 
                           print("You dont have sufficient balance") 
       def check_balance(self): 
                   print(f"Your available balance is: {self.__balance}") 
      def add_interest(self): 
                    interest=int(input("Enter the interest percentage"))
                    interest_amnt=(interest/100)*balance 
                    self.__balance+=interest_amnt 
                    account_number=int(input("Enter your account number:"))
                    balance=int(input("Enter your balanace")) 
b=BankAccount(account_number,balance) 
while True: 
       print("1 check account number 2.deposit 3.withdraw.4.balance 5.interest addition ") 
      choice=int(input("Enter your choice:")) 
      if choice==1: 
            b.check_account_number() 
      elif choice==2: 
            b.deposit() 
      elif choice==3: 
            b.withdraw() 
      elif choice==4: 
            b.check_balance() 
      elif choice==5: 
            b.add_interest()
      else:
            print(“Invalid choice”)
