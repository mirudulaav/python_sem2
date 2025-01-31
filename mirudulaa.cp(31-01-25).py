class TicketBooking: 
    def __init__(self): 
        self.name = input("Enter name: ") 
        self.ph_no = input("Enter phone number: ") 
        self.dob = input("Enter date of birth: ") 
        self.seat_count = int(input("Enter total number of seats: ")) 
        self.num = [str(i) for i in range(1, 21)] 
        self.alpha_fir = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] 
        self.alpha_sec = ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'] 
        self.alpha_eco = ['Y', 'Z'] 
        self.first_class = [j + i for j in self.alpha_fir for i in self.num] 
        self.second_class = [j + i for j in self.alpha_sec for i in self.num] 
        self.economic_class = [j + i for j in self.alpha_eco for i in self.num] 
        self.fir_price = 200 
        self.sec_price = 150 
        self.eco_price = 50 
        self.GST = 0.18 
        self.available_seats = self.first_class + self.second_class + self.economic_class 
 
    def display_available_seats(self): 
        print("\nAvailable Seats:") 
        print("First class:", self.first_class) 
        print("Second class:", self.second_class) 
        print("Economic class:", self.economic_class) 
 
    def calculate_price(self, selected_seats): 
        tot_fir = self.fir_price + (self.fir_price * self.GST) 
        tot_sec = self.sec_price + (self.sec_price * self.GST) 
        tot_eco = self.eco_price + (self.eco_price * self.GST) 
        total_price = 0 
        for seat in selected_seats: 
            seat = seat.strip() 
            if seat in self.first_class: 
                total_price += tot_fir 
            elif seat in self.second_class: 
                total_price += tot_sec 
            elif seat in self.economic_class: 
                total_price += tot_eco 
            else: 
                print(f"Seat {seat} is not available.") 
        return total_price 
 
    def book_tickets(self): 
        self.display_available_seats() 
        selected_seats = input("Select your seats (comma-separated): ").split(',') 
        total_price = self.calculate_price(selected_seats) 
        print(f"\nHi {self.name}..! You have successfully booked {self.seat_count} tickets. Seats: {', '.join(selected_seats)}.") 
        print(f"Your total price: Rs.{total_price:.2f}") 
        return total_price 
 
    def order_snacks(self): 
        snack_prices = {"Popcorn": 100, "Ice Cream": 80, "Puffs": 60, "Tea": 40, "Soft Drinks": 50} 
        snack_total = 0 
        snacks_choice = input("Do you want Snacks? (Yes/No): ").strip().lower() 
        if snacks_choice == "yes": 
            print("\nAvailable Snacks:") 
            for snack, price in snack_prices.items(): 
                print(f"{snack} - Rs.{price}") 
            snack_count = int(input("Enter number of snacks you want: ")) 
            for _ in range(snack_count): 
                snack_name = input("Enter snack name: ").strip() 
                if snack_name in snack_prices: 
                    snack_total += snack_prices[snack_name] 
                else: 
                    print(f"{snack_name} is not available.") 
            print(f"Your snacks price: Rs.{snack_total}") 
        return snack_total 
 
    def generate_bill(self): 
        ticket_price = self.book_tickets() 
        snack_price = self.order_snacks() 
        total_bill = ticket_price + snack_price 
        print(f"Your final total bill: Rs.{total_bill:.2f}") 
 
# Create an instance and run the booking system 
if __name__ == "__main__": 
    booking = TicketBooking() 
    booking.generate_bill()
    
