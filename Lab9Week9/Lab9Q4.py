class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        if item_name in self.items:
            if quantity > 0:
                self.items[item_name]['quantity'] = quantity
            else:
                self.remove_item(item_name)

    def total_cost(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            for item, details in self.items.items():
                print(f"- {item}: {details['quantity']} x ${details['price']:.2f}")
            print(f"Total: ${self.total_cost():.2f}")


cart = ShoppingCart()
cart.add_item("Apple", 1.2, 3)
cart.add_item("Banana", 0.5, 5)
cart.display_cart()
cart.update_quantity("Apple", 2)
cart.display_cart()
cart.remove_item("Banana")
cart.display_cart()
