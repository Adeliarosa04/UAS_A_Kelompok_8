#Script ini dibuat oleh Nabila Shafa
#berfungsi sebagai controller atau pengelola sistem, bukan bagian dari produk langsung.

from typing import List
from produk import ProdukRoti
from interfaces import ProsesProduksi, ProsesPengembangan, ProsesTopping

# ==============================================
# KELAS MANAJEMEN PRODUK
# ==============================================

#Class untuk mengelola produk roti
class ManajerProduk:
    
    def __init__(self):
        self.daftar_produk: List[ProdukRoti] = []
    
    #Menambahkan produk baru ke sistem
    def tambah_produk(self, produk: ProdukRoti) -> None:
        self.daftar_produk.append(produk)
        print(f"Produk {produk.nama} berhasil ditambahkan!")
    
    #Menampilkan semua produk yang tersedia
    def tampilkan_produk(self) -> None:
        if not self.daftar_produk:
            print("Belum ada produk yang terdaftar.")
            return
        
        print("\n=== DAFTAR PRODUK HANARI BAKERY ===")
        for idx, produk in enumerate(self.daftar_produk, 1):
            print(f"\n{idx}. {produk}")
    
    #Menghitung estimasi keuntungan dari produk
    def hitung_keuntungan(self) -> None:
        self.tampilkan_produk()
        if not self.daftar_produk:
            return
        
        try:
            pilihan = int(input("Pilih produk (nomor): ")) - 1
            jumlah = int(input("Masukkan jumlah pcs yang akan diproduksi: "))
            
            if 0 <= pilihan < len(self.daftar_produk):
                produk = self.daftar_produk[pilihan]
                keuntungan = produk.hitung_keuntungan(jumlah)
                print(f"\nEstimasi Keuntungan {jumlah} pcs {produk.nama}:")
                print(f"Total Biaya: Rp{produk.biaya_produksi * jumlah:,.0f}")
                print(f"Total Pendapatan: Rp{produk.harga_jual * jumlah:,.0f}")
                print(f"Keuntungan: Rp{keuntungan:,.0f}")
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Masukkan harus berupa angka!")

    #Menampilkan simulasi proses produksi
    def simulasi_produksi(self) -> None:
        self.tampilkan_produk()
        if not self.daftar_produk:
            return
        
        try:
            pilihan = int(input("Pilih produk (nomor): ")) - 1
            
            if 0 <= pilihan < len(self.daftar_produk):
                produk = self.daftar_produk[pilihan]
                print(f"\n=== SIMULASI PRODUKSI {produk.nama.upper()} ===")
                
                # Proses dasar semua produk
                if isinstance(produk, ProsesProduksi):
                    print("\n1. Pengadonan:")
                    print(produk.aduk())
                    
                    # Proses khusus untuk produk yang perlu pengembangan
                    if isinstance(produk, ProsesPengembangan):
                        print("\n2. Pengembangan:")
                        print(produk.kembangkan())
                    
                    print("\n3. Pemanggangan:")
                    print(produk.panggang())
                    
                    # Proses khusus untuk produk dengan topping
                    if isinstance(produk, ProsesTopping):
                        print("\n4. Topping:")
                        print(produk.beri_topping())
                    
                    print("\n5. Pengemasan:")
                    print(produk.kemas())
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Masukkan harus berupa angka!")
