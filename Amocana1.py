

class Person:
    
    def __init__(self, name, deposit = 1000, loan = 0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Full Name: {self.name}. Current deposit amount: {self.deposit}. Current loan amount: {self.loan}.\n"

class House:

    def __init__(self, ID, price, owner, status = "For sale"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def __str__(self):
        return f"House ID: {self.ID}\nPrice: {self.price}\nOwner Information: {self.owner}\nHouse Status: {self.status}\n"

    def sell_house(self, buyer, deposit, loan, *args):
        if args:
            deposit = deposit + self.price
            self.status = "Sold by Loan"
            self.owner = buyer
            loan = loan + int(*args)
            print(f"Updated Deposit of the Seller: {deposit}\nHouse Updated Status: {self.status}\nNew Owner: {self.owner}\nUpdated Loan of the Buyer: {loan}\n")
        
        else:
            deposit = deposit + self.price
            self.status = "Sold"
            self.owner = buyer
            print(f"Updated Deposit of the Seller: {deposit}\nHouse Updated Status: {self.status}\nNew Owner: {self.owner}\n")
        
        
owner1 = Person("Nikoloz Dumbadze")
print(owner1)

buyer1 = Person("Giorgi Giorgadze")
print(buyer1)

house1 = House("0001", 100, owner1.name)
print(house1)
house1.sell_house(buyer1.name, buyer1.deposit, owner1.loan, 50)

