#Script ini dibuat oleh Hasna Fata
#berisi superclass induk dari semua produk roti dan menyimpan informasi inti dari produk. 
#Beisi Kelas  turunan (subclass) dari ProdukRoti dan juga mengimplementasikan interface produksi sesuai kebutuhan.

from typing import Dict
from interfaces import ProsesProduksi, ProsesPengembangan, ProsesTopping

# ==============================================
# KELAS PRODUK UTAMA
# ==============================================

#SuperClass produk roti
class ProdukRoti:
    def __init__(self, nama: str, kode: str, bahan_baku: Dict[str, float], 
                 biaya_produksi: float, harga_jual: float):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku  # Dictionary bahan: jumlah
        self.biaya_produksi = biaya_produksi  # per pcs
        self.harga_jual = harga_jual  # per pcs
    
    #Menghitung estimasi keuntungan
    def hitung_keuntungan(self, jumlah: int) -> float:
        total_biaya = self.biaya_produksi * jumlah
        total_pendapatan = self.harga_jual * jumlah
        return total_pendapatan - total_biaya
    
    #Membuat daftar bahan baku
    def daftar_bahan(self) -> str:
        return "\n".join([f"- {bahan}: {jumlah}g" for bahan, jumlah in self.bahan_baku.items()])
    
    def __str__(self) -> str:
        return (f"Produk: {self.nama} (Kode: {self.kode})\n"
                f"Harga: Rp{self.harga_jual:,.0f}/pcs\n"
                f"Biaya Produksi: Rp{self.biaya_produksi:,.0f}/pcs\n"
                f"Bahan Baku:\n{self.daftar_bahan()}")

# ==============================================
# KELAS PRODUK SPESIFIK
# ==============================================
#Class untuk produk roti manis
class RotiManis(ProdukRoti, ProsesProduksi, ProsesPengembangan):

    def aduk(self) -> str:
        return "Mengadon adonan roti manis dengan mixer selama 15 menit"
    
    def kembangkan(self) -> str:
        return "Mengembangkan adonan roti manis selama 1 jam"
    
    def panggang(self) -> str:
        return "Memanggang roti manis pada suhu 180°C selama 25 menit"
    
    def kemas(self) -> str:
        return "Mengemas roti manis dalam plastik khusus"

class Croissant(ProdukRoti, ProsesProduksi, ProsesPengembangan):
    """Kelas untuk produk croissant"""
    
    def aduk(self) -> str:
        return "Mengadon adonan croissant dengan teknik laminasi"
    
    def kembangkan(self) -> str:
        return "Mengembangkan adonan croissant selama 2 jam"
    
    def panggang(self) -> str:
        return "Memanggang croissant pada suhu 190°C selama 20 menit"
    
    def kemas(self) -> str:
        return "Mengemas croissant dalam kertas khusus"

class KueKering(ProdukRoti, ProsesProduksi, ProsesTopping):
    """Kelas untuk butter cookies"""
    
    def aduk(self) -> str:
        return "Mengadon adonan kue kering dengan tangan selama 10 menit"
    
    def panggang(self) -> str:
        return "Memanggang kue kering pada suhu 170°C selama 15 menit"
    
    def kemas(self) -> str:
        return "Mengemas kue kering dalam toples kaca"
    
    def beri_topping(self) -> str:
        return "Menambahkan topping choco chips pada kue"

class Muffin(ProdukRoti, ProsesProduksi, ProsesPengembangan, ProsesTopping):
    """Kelas untuk muffin"""
    
    def aduk(self) -> str:
        return "Mengadon adonan muffin dengan whisk selama 8 menit"
    
    def kembangkan(self) -> str:
        return "Mengembangkan adonan muffin selama 30 menit"
    
    def panggang(self) -> str:
        return "Memanggang muffin pada suhu 175°C selama 22 menit"
    
    def kemas(self) -> str:
        return "Mengemas muffin dalam cup kertas"
    
    def beri_topping(self) -> str:
        return "Menambahkan topping keju parut di atas muffin"
