class DaftarMenu:
    def __init__(self):
        self.menu_makanan = []
        self.menu_minuman = []

    def tampilkan_menu_makanan(self):
        print("Daftar Menu Makanan:")
        if self.menu_makanan:
            for index, makanan in enumerate(self.menu_makanan):
                print(f"{index+1}. {makanan}")
        else:
            print("Belum ada menu makanan yang tersedia.")

    def tampilkan_menu_minuman(self):
        print("Daftar Menu Minuman:")
        if self.menu_minuman:
            for index, minuman in enumerate(self.menu_minuman):
                print(f"{index+1}. {minuman}")
        else:
            print("Belum ada menu minuman yang tersedia.")

    def tambahkan_menu_makanan(self, makanan):
        self.menu_makanan.append(makanan)
        print(f"Menu makanan '{makanan}' berhasil ditambahkan.")

    def tambahkan_menu_minuman(self, minuman):
        self.menu_minuman.append(minuman)
        print(f"Menu minuman '{minuman}' berhasil ditambahkan.")

daftar_menu = DaftarMenu()

# Menambahkan menu makanan dan minuman
daftar_menu.tambahkan_menu_makanan("Nasi Goreng")
daftar_menu.tambahkan_menu_makanan("Bakso")
daftar_menu.tambahkan_menu_makanan("Mie Ayam")
daftar_menu.tambahkan_menu_minuman("Es Teh")
daftar_menu.tambahkan_menu_minuman("Es Jeruk")
daftar_menu.tambahkan_menu_minuman("Wedang Uwuh")

# Menampilkan daftar menu makanan dan minuman
daftar_menu.tampilkan_menu_makanan()
print("-" * 20)
daftar_menu.tampilkan_menu_minuman()