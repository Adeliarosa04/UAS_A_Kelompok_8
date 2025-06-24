#Script ini dibuat oleh Fahma Zoeyya
#Bagian ini adalah interface/abstraksi untuk menggambarkan proses produksi roti. 

from abc import ABC, abstractmethod
from typing import Dict, List

# ==============================================
# INTERFACE UNTUK PROSES PRODUKSI (Prinsip SOLID)
# ==============================================

#interface untuk proses produksi bakery
class ProsesProduksi(ABC):
    @abstractmethod
    def aduk(self) -> str:
        pass
    
    @abstractmethod
    def panggang(self) -> str:
        pass
    
    @abstractmethod
    def kemas(self) -> str:
        pass

#interface khusus untuk produk yang perlu pengembangan
class ProsesPengembangan(ABC):
    @abstractmethod
    def kembangkan(self) -> str:
        pass

#Interface khusus untuk produk dengan topping
class ProsesTopping(ABC):
    @abstractmethod
    def beri_topping(self) -> str:
        pass
