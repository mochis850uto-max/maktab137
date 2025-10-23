class Shop:
    def __init__(self, product: str, price: float, expiration_date: int):
        self.product = product
        self.price = price
        self.expiration_date = expiration_date
    def products_sold(self, product_name: str):
        self.product_name = product_name
        sold_out = []
        for product in self.product_name:
            sold_out.append(product)
    def products_without_date(self, product_name: str, date: int):
        self.product_name = product_name
        self.date = date
        if self.date in range(1, 8):
            pass
        else:
            print(f"The {self.product_name} has passed its expiration date.")
    def sale_show(self, sale_product: str, sale_price: float):
        self.sale_product = sale_product
        self.sale_price = sale_price
        sale_counter = 0
        for product in self.sale_product:
            if product == self.sale_product:
                sale_counter += 1
        print(f"The {self.sale_product} was sold for {self.sale_price} in quantities of {sale_counter}.")

store = Shop("milk", 21.2, 9)
store.products_sold("water")
store.products_without_date("flavor", 10)
store.sale_show("ice cream", 2.5)
store.sale_show("ice cream", 2.5)