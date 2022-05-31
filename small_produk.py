from product_delivery import ProductDelivery

class Smallproduct(ProductDelivery):

    def_init_(self, price: int, nama:str):
        super()._init_(price, name)

    def calculate_delivery(self) -> int:
        return self.get_price() + 2000