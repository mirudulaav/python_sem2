class Calculator:
    def calculate(self, a=None, b=None, c=None):
        try:
            if a is not None and b is None and c is None:
                return a ** 2
            elif a is not None and b is not None and c is None:
                return a + b
            elif a is not None and b is not None and c is not None:
                return a * b * c
            else:
                raise ValueError("Invalid number of arguments")
        except TypeError:
            raise ValueError("Arguments must be integers or floats")

calci = Calculator()
print(calci.calculate(4))        
print(calci.calculate(3, 5))     
print(calci.calculate(2, 3, 4))  
