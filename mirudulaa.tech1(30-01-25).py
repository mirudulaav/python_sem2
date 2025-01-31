import re 
class PasswordHelper: 
    def __init__(self): 
        self.name = "" 
        self.department = "" 
        self.password = "" 
        self.security_questions = [ 
            {"question": "What is your favorite color?", "answer": "purple"}, 
            {"question": "What is your pet's name?", "answer": "buddy"} 
        ] 
    def validate_password(self, password): 
        if re.match(r"^(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{1,8}$", password): 
            return True 
        else: 
            print("Invalid Password. Must contain at least one number and one special character. Should 
not be greater than 8 in length.") 
            return False 
 
    def encode_name(self, name): 
        return ''.join(['X' for _ in name]) 
 
    def get_user_input(self): 
        self.name = input("Enter your Name: ") 
        self.department = input("Enter your Department: ") 
 
        attempt = 0 
        while attempt < 3: 
            password = input("Enter your Password: ") 
            retype_password = input("Re-Type your Password: ") 
            if password == retype_password and self.validate_password(password): 
                self.password = password 
                break 
            else: 
                print("Passwords do not match or are invalid. Please try again.") 
                attempt += 1 
         
        if attempt == 3: 
            action = input("Forgot Password or Know Password? (forgot/know): ") 
            if action == "forgot": 
                self.reset_password() 
            else: 
                self.get_user_input() 
 
    def reset_password(self): 
        correct_answers = 0 
        for question in self.security_questions: 
            answer = input(question["question"] + " ") 
            if answer.lower() == question["answer"].lower(): 
                correct_answers += 1 
            else: 
                print("Incorrect answer. Please try again.") 
                self.reset_password() 
                return 
        if correct_answers == len(self.security_questions): 
            print("Your password is:", self.password) 
 
    def display_output(self): 
        print(f"Your Encoded Name is: {self.encode_name(self.name)} – Fresher") 
        print(f"Your Department is: {self.department}") 
        print(f"Your Password is: {'X' * len(self.password)}") 
        print(f"Re-Type your Password: {'X' * len(self.password)}") 
password_helper = PasswordHelper() 
password_helper.get_user_input() 
password_helper.display_output()
