class User:
    def __init__(self, username):
        self.username = username  
        self._password = None  
    
    def set_password(self, password):
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False
        
        has_number = False
        has_special_char = False
        special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
        
        for char in password:
            if char.isdigit():
                has_number = True
            if char in special_characters:
                has_special_char = True
        
        if not has_number or not has_special_char:
            print("Password must contain at least one number and one special character.")
            return False
        
        self._password = password  
        return True
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self._password
    
    def check_password(self, input_password):
        return input_password == self._password

name = input("Enter the Username: ") 
user = User(name)
password = input("Enter the Password: ")
if user.set_password(password):  
    print("Password set successfully.")
else:
    print("Password not set due to invalid criteria.")

input_password = input("Enter the password to verify: ")
if user.check_password(input_password):
    print(f"Password verified successfully for {user.get_username()}.")
else:
    print("Password is incorrect.")
