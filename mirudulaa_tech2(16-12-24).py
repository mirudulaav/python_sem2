class Product:
    def __init__(self, name, price, stock):
        self._name = name
        self._price = None
        self._stock = None
        self.set_price(price)
        self.set_stock(stock)

    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Price must be greater than 0.")

    def set_stock(self, stock):
        if isinstance(stock, int) and stock >= 0:
            self._stock = stock
        else:
            print("Stock must be a non-negative integer.")

    def get_stock(self):
        return self._stock
    
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price


name = input("Enter the product name: ")
price = float(input("Enter the price: "))
stock = int(input("Enter the stock quantity: "))

product = Product(name, price, stock)

print(f"\nProduct Name: {product.get_name()}")
print(f"Product Price: {product.get_price()}")
print(f"Product Stock: {product.get_stock()}")
