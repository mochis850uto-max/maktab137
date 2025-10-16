class Cake:
    def __init__(self, flavor: str, size, price: float):
        self.flavor = flavor
        self.size = size
        self.price = price
    def describe(self):
        print(f"Cake with flavor {self.flavor} ,size of {self.size} and price of {self.price}")
c = Cake("Chocolate", "Medium", 1.2)
c.describe()
