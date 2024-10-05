class DaftarMenu:
    def __init__(self):
        self.makanan = []
        self.minuman = []

    def tampilkan_menu_makanan(self):
        if not self.makanan:
            print("Daftar menu makanan kosong.")
        else:
            print("Daftar Menu Makanan:")
            for makanan in self.makanan:
                print(f"- {makanan}")

    def tampilkan_menu_minuman(self):
        if not self.minuman:
            print("Daftar menu minuman kosong.")
        else:
            print("Daftar Menu Minuman:")
            for minuman in self.minuman:
                print(f"- {minuman}")

    def tambah_menu_makanan(self, nama_makanan):
        self.makanan.append(nama_makanan)
        print(f"{nama_makanan} telah ditambahkan ke daftar menu makanan.")

    def tambah_menu_minuman(self, nama_minuman):
        self.minuman.append(nama_minuman)
        print(f"{nama_minuman} telah ditambahkan ke daftar menu minuman.")


# Contoh penggunaan
menu = DaftarMenu()

while True:
    print("\nMenu:")
    print("1. Tambah Menu Makanan")
    print("2. Tambah Menu Minuman")
    print("3. Tampilkan Menu Makanan")
    print("4. Tampilkan Menu Minuman")
    print("5. Keluar")
    
    pilihan = input("Pilih opsi (1-5): ")
    
    if pilihan == "1":
        nama_makanan = input("Masukkan nama makanan: ")
        menu.tambah_menu_makanan(nama_makanan)
    elif pilihan == "2":
        nama_minuman = input("Masukkan nama minuman: ")
        menu.tambah_menu_minuman(nama_minuman)
    elif pilihan == "3":
        menu.tampilkan_menu_makanan()
    elif pilihan == "4":
        menu.tampilkan_menu_minuman()
    elif pilihan == "5":
        print("Terima kasih, sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
