#1
class CheckString:
    def __init__(self, string):
        self.string=string
        self.alpha=0
        self.num=0
        self.special=0
    def checkcount(self):
        for i in self.string:
            if i.isalpha():
                self.alpha+= 1
            elif i.isdigit():
                self.num+= 1
            else:
                self.special+= 1
    def displaycount(self):
        print(f"Aplhabet count: {self.alpha}")
        print(f"Number count: {self.num}")
        print(f"Special character count: {self.special}")

string= input("Enter Required String:")
count=CheckString(string)
count.checkcount()
count.displaycount()

#2
class StringValidator:
    def __init__(self, input_string):
        self.input_string = input_string
        self.alpha=0
        self.special=0
    def validate_string(self):
        for char in self.input_string:
            if char.isalpha():
                self.alpha+=1
            elif not char.isalnum():
                self.special+=1
        return self.alpha*self.special
    def display_result(self):
        if self.validate_string():
            print("The string contains both alphabets and special characters.")
        else:
            print("The string does not contain both.")
input_string =input("Enter string:")
validator = StringValidator(input_string)
validator.display_result()

        
