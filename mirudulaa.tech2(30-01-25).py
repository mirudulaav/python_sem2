import re
class UserInput:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.email = ""
        self.n = 0

    def validate_name(self, name):
        if re.match(r"^(?=.*[0-9])(?=.*[@#$%^&+=])[A-Za-z0-9@#$%^&+=]+$", name):
            self.name = name
            return True
        else:
            print("Invalid name! It must contain at least one number and one special character.")
            return False

    def validate_password(self, password):
        if re.match(r"^[A-Za-z#_@]{1,8}$", password):
            self.password = password
            return True
        else:
            print("Invalid password! It must contain only letters and #, _, @. Max length: 8.")
            return False

    def validate_email(self, email):
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            self.email = email
            return True
        else:
            print("Invalid email! Enter a valid email format.")
            return False

    def get_user_input(self):
        while True:
            name = input("Enter your Name: ")
            if self.validate_name(name):
                break
        
        while True:
            password = input("Enter your Password: ")
            if self.validate_password(password):
                break
        
        while True:
            email = input("Enter your Email Address: ")
            if self.validate_email(email):
                break
        
        while True:
            try:
                self.n = int(input("How many times do you want to Print? "))
                break
            except ValueError:
                print("Invalid input! Enter a valid number.")
    
    def display_output(self):
        print(f"\n{self.name} Wants to Print {self.n} Times and send Mail to {self.email}.")
        print(f"Your password {self.password} will be encrypted and will be stored.")

if __name__ == "__main__":
    user = UserInput()
    user.get_user_input()
    user.display_output()
