class Transaction:
    def __init__(self, name_product=None, quantity=None, consumer=None, date=None):
        self.name_product = name_product
        self.quantity = quantity
        self.consumer = consumer
        self.date = date

    def import_into_warehouse(self):
        pass

    def remove_from_warehouse(self):
        pass
