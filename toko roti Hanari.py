from abc import ABC, abstractmethod
from typing import Dict, List

# ==============================================
# ANTARMUKA UNTUK PROSES PRODUKSI (Prinsip SOLID)
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
# ==============================================
# KELAS PRODUK UTAMA
# ==============================================
class ProdukRoti:
    """Kelas dasar untuk semua produk roti"""
    
    def __init__(self, nama: str, kode: str, bahan_baku: Dict[str, float], 
                 biaya_produksi: float, harga_jual: float):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku  # Dictionary bahan: jumlah
        self.biaya_produksi = biaya_produksi  # per pcs
        self.harga_jual = harga_jual  # per pcs
    
    def hitung_keuntungan(self, jumlah: int) -> float:
        """Menghitung estimasi keuntungan"""
        total_biaya = self.biaya_produksi * jumlah
        total_pendapatan = self.harga_jual * jumlah
        return total_pendapatan - total_biaya
    
    def daftar_bahan(self) -> str:
        """Membuat daftar bahan baku"""
        return "\n".join([f"- {bahan}: {jumlah}g" for bahan, jumlah in self.bahan_baku.items()])
    
    def __str__(self) -> str:
        return (f"Produk: {self.nama} (Kode: {self.kode})\n"
                f"Harga: Rp{self.harga_jual:,.0f}/pcs\n"
                f"Biaya Produksi: Rp{self.biaya_produksi:,.0f}/pcs\n"
                f"Bahan Baku:\n{self.daftar_bahan()}")
