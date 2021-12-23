class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.

        total = 0
        for item in self.items:
            total += item["price"]
        return total
        # return sum([item["price"] for item in self.items])


store1 = Store("Shooping")
store1.add_item("roxana", 50)
store1.add_item("yerandy", 80)
print(store1.stock_price())
