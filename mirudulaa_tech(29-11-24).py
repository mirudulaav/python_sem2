##1##
class Library:
    def __init__(self, name, genre, copy):
        self.name = name
        self.genre = genre
        self.copy = copy
    def displayBookInfo(self):
        print(f"Name: {self.name}\nGenre: {self.genre}\nCopy: {self.copy}")

class Member:
    def __init__(self, mem_name, mem_id):
        self.mem_name = mem_name
        self.mem_id = mem_id
    def displayMemInfo(self):
        print(f"Member Name: {self.mem_name}\nMember ID: {self.mem_id}")

class LibraryManagement(Library, Member):
    def __init__(self, mem_name, mem_id, name, genre, copy):
        Library.__init__(self, name, genre, copy)
        Member.__init__(self, mem_name, mem_id)
    def displayLib(self):
        self.displayBookInfo()  
        self.displayMemInfo()   

lib = LibraryManagement("Megha", 1877, "Percy Jackson", "Fantasy", 26)
lib.displayLib()

##2##
class Restaraunt:
    def __init__(self, name, item, price):
        self.name= name
        self.item= item
        self.price= price
    def  displayRestarauntDetails(self):
        print(f"RestarauntName: {self.name}\nItem: {self.item}\nPrice: {self.price}")

class Delivery:
    def __init__(self, time, ridername, number):
        self.time= time
        self.ridername= ridername
        self.number= number
    def displayDeliveryDetails(self):
        print(f"Delivery Time: {self.time}\nRider's Name: {self.ridername}\nRider's Num: {self.number}")

class OrderDetails(Restaraunt, Delivery):
    def __init__(self, name, item, price, time, ridername, number):
        Restaraunt.__init__(self, name, item, price)
        Delivery.__init__(self, time, ridername, number)
    def displayOrder(self):
        self.displayRestarauntDetails()
        self.displayDeliveryDetails()

ord1=OrderDetails("Green Park", "VegNoodles", 90, "30 min", "Niki", 1234567894)
ord1.displayOrder()
        

    
