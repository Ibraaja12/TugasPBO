class Pegawai:
    def __init__(self, nik, nama):
        self.nik = nik
        self.nama = nama

    def get_info(self):
        return f"NIK: {self.nik}, Nama: {self.nama}"


class Produk:
    def __init__(self, kode_produk, nama_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga

    def get_info(self):
        return f"Kode Produk: {self.kode_produk}, Nama Produk: {self.nama_produk}, Harga: {self.harga}"


class Struk:
    def __init__(self, pegawai, produk, jumlah):
        self.pegawai = pegawai
        self.produk = produk
        self.jumlah = jumlah
        self.total_harga = produk.harga * jumlah

    def get_info(self):
        return (f"Struk:\nPegawai: {self.pegawai.nama} (NIK: {self.pegawai.nik})\n"
                f"Produk: {self.produk.nama_produk} (Kode: {self.produk.kode_produk})\n"
                f"Jumlah: {self.jumlah}\nTotal Harga: {self.total_harga}")


def main():
    pegawai_list = []
    produk_list = []

    while True:
        print("\nPilih opsi:")
        print("1. Buat Pegawai")
        print("2. Buat Produk")
        print("3. Buat Struk")
        print("4. Tampilkan Semua Pegawai")
        print("5. Tampilkan Semua Produk")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            nik = input("Masukkan NIK: ")
            nama = input("Masukkan Nama: ")
            pegawai = Pegawai(nik, nama)
            pegawai_list.append(pegawai)
            print("\nPegawai berhasil dibuat:")
            print(pegawai.get_info())

        elif pilihan == "2":
            kode_produk = input("Masukkan Kode Produk: ")
            nama_produk = input("Masukkan Nama Produk: ")
            harga = float(input("Masukkan Harga: "))
            produk = Produk(kode_produk, nama_produk, harga)
            produk_list.append(produk)
            print("\nProduk berhasil dibuat:")
            print(produk.get_info())

        elif pilihan == "3":
            if pegawai_list and produk_list:
                print("\nPilih Pegawai:")
                for index, pegawai in enumerate(pegawai_list):
                    print(f"{index + 1}. {pegawai.get_info()}")
                pegawai_index = int(input("Pilih Pegawai (nomor): ")) - 1

                print("\nPilih Produk:")
                for index, produk in enumerate(produk_list):
                    print(f"{index + 1}. {produk.get_info()}")
                produk_index = int(input("Pilih Produk (nomor): ")) - 1

                jumlah = int(input("Masukkan Jumlah Produk: "))
                struk = Struk(pegawai_list[pegawai_index], produk_list[produk_index], jumlah)
                print("\nStruk berhasil dibuat:")
                print(struk.get_info())
            else:
                print("\nSilakan buat Pegawai dan Produk sebelum membuat Struk.")

        elif pilihan == "4":
            print("\nDaftar Pegawai:")
            for pegawai in pegawai_list:
                print(pegawai.get_info())

        elif pilihan == "5":
            print("\nDaftar Produk:")
            for produk in produk_list:
                print(produk.get_info())

        elif pilihan == "6":
            print("Keluar...")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()