#Script ini dibuat oleh Adelia Rosa 
#sebagai main loop aplikasi berbasis menu CLI (Command Line Interface)
#Menyediakan berbagai pilihan menu

from produk import RotiManis, Croissant, KueKering, Muffin
from manajer import ManajerProduk

# ==============================================
# FUNGSI UTAMA DAN MENU
# ==============================================

#Fitur utama untuk menjalankan program
def jalankan_program():
    manajer = ManajerProduk()
    
    # Data contoh produk awal
    contoh_produk = [
        RotiManis(
            nama="Roti Manis Coklat",
            kode="RM001",
            bahan_baku={"Tepung terigu": 500, "Gula": 100, "Telur": 2, "Ragi": 10, "Coklat": 50},
            biaya_produksi=8000,
            harga_jual=15000
        ),
        Croissant(
            nama="Croissant Almond",
            kode="CR002",
            bahan_baku={"Tepung terigu": 400, "Mentega": 200, "Susu": 100, "Gula": 50, "Almond": 30},
            biaya_produksi=12000,
            harga_jual=25000
        ),
        KueKering(
            nama="Kue Kering Coklat",
            kode="KK003",
            bahan_baku={"Tepung terigu": 300, "Mentega": 150, "Gula halus": 80, "Kuning telur": 2, "Coklat": 100},
            biaya_produksi=5000,
            harga_jual=10000
        ),
        Muffin(
            nama="Muffin Blueberry",
            kode="MF004",
            bahan_baku={"Tepung terigu": 350, "Gula": 120, "Telur": 2, "Susu": 150, "Blueberry": 100, "Keju": 50},
            biaya_produksi=7000,
            harga_jual=12000
        )
    ]
    
    # Menambahkan contoh produk
    for produk in contoh_produk:
        manajer.tambah_produk(produk)
    
    while True:
        print("\n=== SISTEM INFORMASI HANARI BAKERY ===")
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Estimasi Keuntungan")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")
        
        try:
            pilihan = int(input("Pilih menu (1-5): "))
            
            if pilihan == 1:
                print("\n=== TAMBAH PRODUK BARU ===")
                nama = input("Nama Produk: ")
                kode = input("Kode Produk: ")
                
                bahan = {}
                print("\nMasukkan Bahan Baku (ketik 'selesai' untuk berhenti):")
                while True:
                    nama_bahan = input("Nama Bahan: ")
                    if nama_bahan.lower() == 'selesai':
                        break
                    jumlah = float(input("Jumlah (gram): "))
                    bahan[nama_bahan] = jumlah
                
                biaya = float(input("Biaya Produksi per pcs: Rp"))
                harga = float(input("Harga Jual per pcs: Rp"))
                
                print("\nPilih Jenis Produk:")
                print("1. Roti Manis")
                print("2. Croissant")
                print("3. Kue Kering")
                print("4. Muffin")
                pilihan_jenis = int(input("Pilihan (1-4): "))
                
                if pilihan_jenis == 1:
                    produk = RotiManis(nama, kode, bahan, biaya, harga)
                elif pilihan_jenis == 2:
                    produk = Croissant(nama, kode, bahan, biaya, harga)
                elif pilihan_jenis == 3:
                    produk = KueKering(nama, kode, bahan, biaya, harga)
                elif pilihan_jenis == 4:
                    produk = Muffin(nama, kode, bahan, biaya, harga)
                else:
                    print("Pilihan tidak valid!")
                    continue
                
                manajer.tambah_produk(produk)
            
            elif pilihan == 2:
                manajer.tampilkan_produk()
            
            elif pilihan == 3:
                manajer.hitung_keuntungan()
            
            elif pilihan == 4:
                manajer.simulasi_produksi()
            
            elif pilihan == 5:
                print("Terima kasih telah menggunakan sistem Hanari Bakery!")
                break
            
            else:
                print("Pilihan harus antara 1-5!")
        
        except ValueError:
            print("Masukkan harus berupa angka!")

if __name__ == "__main__":
    jalankan_program()
