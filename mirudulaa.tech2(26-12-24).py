class SimpleCalculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

def main():
    calc = SimpleCalculator()
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            op = input("Enter operation (+, -, *, /): ")
            if op == '+':
                result = calc.add(num1, num2)
            elif op == '-':
                result = calc.subtract(num1, num2)
            elif op == '*':
                result = calc.multiply(num1, num2)
            elif op == '/':
                result = calc.divide(num1, num2)
            else:
                print("Invalid operation.")
                continue
            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input.")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()
      
        
