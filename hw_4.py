class Product:

    def __init__(self, barcode, warehouse, brand):
        self.barcode = barcode
        self.warehouse = warehouse
        self.brand = brand

    def buy(self, customer_id, quantity):
        pass


class Shoe(Product):
    def __init__(self, barcode, warehouse, brand, model, gender, sizes):
        super().__init__(barcode, warehouse, brand)
        self.model = model
        self.gender = gender
        self.sizes = sizes

    def buy(self, customer_id, quantity, size):
        super().buy()
        pass


class Sandal(Shoe):
    pass


