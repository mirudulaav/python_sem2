class Pizza_Size:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    def check_budget(self, budget):
        if not isinstance(budget,(int,float)) or budget<0:
            raise ValueError("Budget should not be negative")
    def calculate_balance(self, budget):
        return budget-self.price
    def suggest_size(self, budget):
        try:
            self.check_budget(budget)
            if budget>self.price:
                print(f"You can have {self.name}")
                print(f"Your remaining balance is {self.calculate_balance(budget)}")
            elif budget==self.price:
                print(f"You can have {self.name}. No balance")
            else:
                print(f"You can't afford any. You should have {self.price-budget}")
        except ValueError as ve:
            print(ve)
small=Pizza_Size('small', 99)
medium=Pizza_Size('large', 150)
large=Pizza_Size('large', 200)
sizes=['small', 'medium', 'large']
try:
    budget=float(input("Enter your budget:"))
    for s in sizes:
        s.suggest_size(budget)
except ValueError:
    print("Budget must be numerical")
