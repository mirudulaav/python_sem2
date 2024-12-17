import random
class Customer:
    def __init__(self, customer_id, name, phoneno):
        self.customer_id= customer_id
        self.name= name
        self.phoneno= phoneno

    def generate_rand_id(self):
        c_id= random.randint(1000, 9999)
        return f"TICK{c_id}"

    def verify_customer_id(customer_id):
        for i in customer_id:
            if customer_id[0:4]=="TICK" and i[4:8].isdigit():
                print("Valid")
            else:
                print("Invalid")

class TicketBooking:
    def __init__(self):
        self.events={"Concert":{"price":1500,"seats":1000},"Movie":{"price":500,"seats":1000},"Drama":{"price":150,"seats":2000}}
        self.booked_tickets=[]

    def view_events():
        for events, details in self.events.items():
            print(f"{events}: {details['price']} per ticket {details['seats']} seats are available")

    def book_tickets(self, event_name, quantity, customer):
        if event_name in self.events:
            event=self.events[event_name]
            if event['seats'] >= quantity:
                totalprice= event['price']*quantity
                event['seats']-= quantity
                self.booked_tickets.append({"Customer ID:", customer.customer_id, "Event Name:", event_name, "Quantity:", quantity, "Total Price:", totalprice,})
            else:
                print("All Seats are Booked!!")
        else:
            print("Event is not Available")

    def view_tickets(self, customer):
        print("****TICKET BOOKING INFORMATION****")
        c_ticket= [t for t in self.booked_tickets if t["Customer ID"]==customer.customer_id]
        if not c_ticket:
            print("No tickets booked")
        else:
            for tick in c_ticket:
                print(f"Event:{tick['event']}, Quantity:{tick['quantity']}, Total Cost:{tick['totalprice']}")
    
    
print(f"Welcome to TICKET BOOKING APPLICATION")
customer_id=input("Enter the customer id:")

if Customer.verify_customer_id(customer_id):
    name= input("Enter your Name:")
    phoneno= int(input("Enter your Phone No:"))
    customer= Customer(customer_id, name, phoneno)
    print("BOOKING DETAILS")
else:
    print("Invalid!....Please REGISTER")
    name= input("Enter Name:")
    phoneno=int(input("Enter Phone Num:"))
    customer_id= Customer.generate_rand_id(self)
    customer=Customer(customer_id, name, phoneno)
    print("Your Customer ID is", customer_id)

while True:
    print("## Booking INFO ##")
    print("1.View Events\n2.Book Tickets\n3.View my booking Details\n4.Exit")
    choice=int(input("Enter option:"))
    if choice==1:
        book.view_events()
    elif choice==2:
        event_name= input("Enter the Event Name:")
        quantity=int(input("Enter the number of tickets:"))
        book.book_tickets(event_name, quantity, customer)                      
    elif choice==3:
        book.view_tickets()
    elif choice==4:
        quit()
    else:
        print("Option not available")
        
        
