#2
class PasswordProcessor:
    def __init__(self, password):
        self.password = password

    def break_number(self):
        result = " "
        for char in self.password:
            if char.isdigit():
                break
            result += char
        print("Your Output will Break here -", result)

    def skip_numbers(self):
        result = " "
        for char in self.password:
            if not char.isdigit():
                result += char
        print("Your output will continue here -", result)

if __name__ == "__main__":
    password1 = input("Enter your input: ")
    processor1 = PasswordProcessor(password1)
    processor1.break_number()

    password2 = input("Enter your input: ")
    processor2 = PasswordProcessor(password2)
    processor2.skip_numbers()
