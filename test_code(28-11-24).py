class Inventory:
    def getInventoryInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
        self.count=int(input("Enter the Count:"))
    def displayInventoryInfo(self):
        print("ID = ",self.id,"\nName = ",self.name,"\nCount = ",self.count)

class Inventory:                                         
    def init(self,prodID,prodName,prodCount):
        self.prodID=prodID
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print(f"Product ID = {self.prodID}")
        print(f"Product Name = {self.prodName}")
        print(f"Product Count = {self.prodCount}")

prod=Inventory(3412,"Pencil",50)
prod.display()

class Inventory:
    def _init_(self):
        self.prodId = input("Enter the ProdId :")
        self.prodname = input("Enter the ProdName:")
        self.prodcount = input("Enter the ProdCount:")

class Products(Inventory):
    def display(self):
        print("ProdId=",self.prodId,"\nProdName=",self.prodname,"\nProdCount=",self.prodcount)

p=Products()
p.display()
