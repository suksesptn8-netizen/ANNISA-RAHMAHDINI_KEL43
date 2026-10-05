def judul(): 
    return "PROGRAM_DATA_BELANJA" 

def hitung_subtotal(harga, jumlah): 
    return harga * jumlah 

def tampilkan_pesan(pesan): 
    print(pesan) 

class Keranjang: 
    def __init__(self): 
        self.barang = [] 
        
    def tambah_barang(self, nama, harga, jumlah): 
        self.barang.append([nama, harga, jumlah]) 
        
    def hitung_total(self): 
        total = 0 
        for barang in self.barang: 
            total += hitung_subtotal(barang[1], barang[2]) 
        return total 
        
    def tampilkan_barang(self): 
        if len(self.barang) == 0: 
            tampilkan_pesan("Keranjang masih kosong.") 
        else: 
            for nomor, barang in enumerate(self.barang, start=1): 
                subtotal = hitung_subtotal(barang[1], barang[2]) 
                print(f"{nomor}. {barang[0]} - Rp{subtotal}") 

keranjang = Keranjang() 
print(judul()) 

while True: 
    print(""" 
    1. Tambah barang 
    2. Lihat keranjang 
    3. Lihat total belanja 
    4. Keluar 
    """) 
    pilihan = input("Pilih menu: ") 
    
    if pilihan == "1": 
        nama = input("Nama barang: ") 
        harga = int(input("Harga barang: Rp")) 
        while harga <= 0: 
            harga = int(input("Harga harus lebih dari 0. Masukkan kembali: Rp")) 
        jumlah = int(input("Jumlah barang: ")) 
        while jumlah <= 0: 
            jumlah = int(input("Jumlah harus lebih dari 0. Masukkan kembali: ")) 
        keranjang.tambah_barang(nama, harga, jumlah) 
        tampilkan_pesan("Barang berhasil ditambahkan.") 
        
    elif pilihan == "2": 
        keranjang.tampilkan_barang() 
        
    elif pilihan == "3": 
        print(f"Total belanja: Rp{keranjang.hitung_total()}") 
        
    elif pilihan == "4": 
        tampilkan_pesan("Program selesai.") 
        break 
        
    else: 
        tampilkan_pesan("Pilihan tidak tersedia.") 

print("Kelompok 43")
