class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    def sell(self, amount):
        if amount <= 0:
            print("sale amount must be positive")
            return
        if amount > self.quantity:
            print(f"not enough stock to sell {amount} units of {self.name}")
        else:
            self.quantity -= amount
            print(f"sold {amount} units of {self.name}")
    def restock(self, amount):
        self.quantity += amount
        print(f"restocked {amount} units of {self.name}. Total: {self.quantity}")
        if amount <= 0:
            print("restock amount must be positive")
            return
    def display_info(self):
        print(f"Name product: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}")

class Inventory:
    def __init__(self, products = []):
        self.product = products

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"aded {product.name} to inventory.")
    
    def update_product(self, product_name: str, new_price: float):
        for product in self.products:
            if product.name == product_name:
                product.price = new_price
                print(f"updated price for {product_name} to {new_price}")
                return
            else:
                print(f"product {product_name} not found in inventory")


p1 = Product("phone", 165.2, 7)
p1.sell(1)
p1.restock(0)
p1.display_info()