from pemukul import Pemukul
from penembak import Penembak
from pengendara import Pengendara


menabrak = Pengendara("Berlari",40)
print(menabrak.menyerang())

memukul = Pemukul("Memukul kencang",40)
print(memukul.menyerang())

menembak = Penembak("Tembakan",60)
print(menembak.menyerang())