## Papa Pizza Ordering System
class Pizza: 
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Pizza_Arr: 
    def main():
        pizzas = {
            "Pepperoni": Pizza("Pepperoni", 21.00),
            "Chicken Supreme": Pizza("Chicken Supreme", 23.50),
            "BBQ Meatlovers": Pizza("BBQ Meatlovers", 25.50),
            "Veg Supreme": Pizza("Veg Supreme", 22.50),
            "Hawaiian": Pizza("Hawaiian", 19.00),
            "Margherita": Pizza("Margherita", 18.50)
        }
        
class Orders: 
    def __init__(self):
        self.pizza = []
        self.delivery = False
        self.loyalty = False
        self.subtotal = 0.0
        
    def add(self, pizza, quantity):
        self.pizzas.append((pizza, quantity))
        self.subtotal += pizza.price * quantity
        
    def delv(self, delivery):
        self.delivery = delivery
        if delivery:
            self.subtotal += 8.00 
            
    def loy(self,loyalty):
        self.loyalty = loyalty
        
    def discount(self):
        if self.subtotal > 100 or self.loyalty:
            return self.subtotal * 0.95 
        return self.subtotal
    
    def gst(self):
        return self.discount() * 0.1
    
    def total(self):
        return self.discount() + self.gst
    
    def order_details(self):
        print("\nDetails: ")
        for pizza, quantity in self.pizzas: 
            print(f"{pizza.name} | Quantity: {quantity}")
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Delivery: ${self.delivery * 8.0:.2f}")
        print(f"GST: ${self.gst():.2f}")
        print(f"Total: ${self.total():.2f}\n")
        
    def main():
        while True:  
            print("\nOrdering Sys...")
            print("1. View Menu")
            print("2. Add Order")
            print("3. Process Order")
            print("4. Generate Daily Sales Summary")
            print("5. Exit")
            inp = input("Enter User Choice (1-5): ")
            
            if not (inp.isdigit() and 1 <= int(inp) <= 5):
                print("Invalid Input")
                continue
    
            if inp == "1":
                #input no 1
                print("\n Pepperoni - $21.00\n Chicken Supreme - $23.50\n BBQ Meatlovers - $25.50\n Veg Supreme - $22.50\n Hawaiian - $19.00\n Margherita - $18.50\n") 
                
    main()