from karakter import Karakter

class Pemukul(Karakter):
    
    def __init__(self, nama: str, power: int):
        super().__init__(nama, power)
    
    def menyerang(self)->str:
        print("Mengeluarkan ",self.get_nama(),self.get_power(),"power memukul")