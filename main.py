## Papa Pizza Ordering System
#I just thought it would be cool to import time
import time

# -------------------------
# Classes
# -------------------------
class Pizza: 
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Orders: 
    def __init__(self):
        self.pizza = []
        self.delivery = False
        self.loyalty = False
        self.subtotal = 0.0
    
    #[option 2 from menu] Program for selecting pizzas for the order 
    def add(self, pizza, quantity):
        self.pizza.append((pizza, quantity))
        self.subtotal += pizza.price * quantity
    
    #[option 2 from menu] optional delivery ($8)
    def delv(self, delivery):
        self.delivery = delivery
        if delivery:
            self.subtotal += 8.00 
    
    #[option 2 from menu] optional loyalty card inclusion (10% off)
    def loy(self,loyalty):
        self.loyalty = loyalty
     
    #if a loyalty card or the order is about $100 5% discount is applied  
    def discount(self):
        if self.subtotal > 100 or self.loyalty:
            return self.subtotal * 0.95 
        return self.subtotal
    
    #adding the gst tax to when selecting the order (10%)
    def gst(self):
        return self.discount() * 0.1
    
    #adding the discount and gst to get the total
    def total(self):
        return self.discount() + self.gst()
    
    #printing out the order details
    def order_details(self):
        print("\nDetails: ")
        for pizza, quantity in self.pizza: 
            print(f"{pizza.name} | Quantity: {quantity}")
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Delivery: ${self.delivery * 8.0:.2f}")
        print(f"GST: ${self.gst():.2f}")
        print(f"Total: ${self.total():.2f}\n")
# -------------------------
# Subprograms
# -------------------------
def main():
    pizzas = {
        "pepperoni": Pizza("Pepperoni", 21.00),
        "chicken supreme": Pizza("Chicken Supreme", 23.50),
        "bbq meatlovers": Pizza("BBQ Meatlovers", 25.50),
        "veg supreme": Pizza("Veg Supreme", 22.50),
        "hawaiian": Pizza("Hawaiian", 19.00),
        "margherita": Pizza("Margherita", 18.50)
    }  
    
    order = Orders()
    while True:  
        print("\nOrdering System")
        print("1. View Menu")
        print("2. Add Order")
        print("3. Process Order")
        print("4. Generate Daily Sales Summary")
        print("5. Exit")
        choice = input("Enter User Choice (1-5): ")
        
        if choice == "1":
            print("\nMenu:")
            for pizza_name, pizza in pizzas.items():
                print(f"{pizza.name} - ${pizza.price:.2f}")
                
        elif choice == "2":
            pizza_type = input("Enter pizza name: ").lower()
            quantity = int(input("How many of this pizza do you want? "))
            if pizza_type in pizzas:
                order.add(pizzas[pizza_type], quantity)
            else:
                print(f"Invalid input: {pizza_type}")
            
            delivery = input("Do you want delivery? (y/n): ").lower() == "y"
            order.delv(delivery)
            loyalty = input("Do you have a loyalty card? (y/n): ").lower() == "y"
            order.loy(loyalty)
            order.order_details()
            
        elif choice == "3":
            if order.total() == 0:
                print("No orders to process")
            else:
                order_summary = f"\nOrder Summary: \n"
                for pizza, quantity in order.pizza:
                    order_summary += f"{pizza.name} | Quantity: {quantity}\n"
                order_summary += f"Subtotal: ${order.subtotal:.2f}\n"
                order_summary += f"Delivery: ${order.delivery * 8.0:.2f}\n"
                order_summary += f"GST: ${order.gst():.2f}\n"
                order_summary += f"Total: ${order.total():.2f}\n"
                
                fileext = "order_summary.txt"
                with open(fileext, "a") as file:
                    file.write("---------------------------------")
                    file.write(order_summary)
                
                print(f"Order summary saved to {fileext}")
        
        elif choice == "4":
            fileext1 = "order_summary.txt"
            with open(fileext1, "r") as file:
                file_content = file.read()
                print("Daily Sales Summary: \n", file_content)
        
        elif choice == "5":
            time.sleep(1)
            print("Exiting...")
            time.sleep(3)
            break
        
        else:
            print("Invalid Input")

# -------------------------
# Main program
# -------------------------

if __name__ == "__main__":
    main()
