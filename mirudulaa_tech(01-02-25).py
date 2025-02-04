class BookStall:
    def __init__(self, book_name, customer_id, book_price):
        self.book_name = book_name
        self.customer_id = customer_id
        self.book_price = book_price
        self.discount = 0

    def get_book_details(self):
        while True:
            self.book_name = input("Enter your Book Name: ").strip()
            if self.book_name:
                break
            print("Book Name cannot be empty. Please enter a valid book name.")
        
        while True:
            try:
                self.customer_id = int(input("Enter your Customer ID: ").strip())
                if self.customer_id > 0:
                    break
                print("Customer ID must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric Customer ID.")

        while True:
            try:
                self.book_price = float(input("Enter the Price of the Book: ").strip())
                if self.book_price > 0:
                    break
                print("Price must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric price.")

    def calculate_discount(self):
        if 1 <= self.customer_id <= 100:
            self.discount = 50
        elif 101 <= self.customer_id <= 300:
            self.discount = 30
        elif 301 <= self.customer_id <= 400:
            self.discount = 20
        elif 401 <= self.customer_id <= 500:
            self.discount = 10
        else:
            self.discount = 0

    def display_details(self):
        discounted_price = self.book_price * (1 - self.discount / 100)
        print(f"\nPrice of the Book is {self.book_price:.2f} MRP")
        print(f"You are eligible for a Discount of {self.discount}%")
        print(f"Your discounted Price for the Book is {discounted_price:.2f} MRP")

    def run(self):
        while True:
            self.get_book_details()
            self.calculate_discount()
            self.display_details()
            
            cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("Thank you for visiting Zampa's Book Stall!")
                break

if __name__ == "__main__":
    book_stall = BookStall("", 0, 0.0)
    book_stall.run()
