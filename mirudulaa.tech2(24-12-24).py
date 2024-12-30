class Product:
    def __init__(self, base_price, discount_percentage=0, tax_percentage=0):
        if base_price < 0 or discount_percentage < 0 or tax_percentage < 0:
            raise ValueError("Negative values are not allowed")
        self.base_price = base_price
        self.discount_percentage= discount_percentage
        self.tax_percentage= tax_percentage

    def calculate_final_price(self):
        discount_amount = self.base_price * (self.discount_percentage / 100)
        discounted_price = self.base_price - discount_amount
        tax_amount = discounted_price * (self.tax_percentage / 100)
        final_price = discounted_price + tax_amount
        return final_price

pdt1 = Product(100, 10, 5)
print(product1.calculate_final_price())  

pdt2 = Product(50, 0, 8)
print(product2.calculate_final_price())  
