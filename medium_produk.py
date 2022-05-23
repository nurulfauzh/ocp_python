from zlib import DEF_BUF_SIZE
from produk_delivery import ProdukDelivery

class MediumProduk (ProdukDelivery):

    def __init__ (self, price : int, name : str ):
        super().__init__(price, name)

    def calculate_delivery(self) -> int:
        return self.get_price() + 2500
