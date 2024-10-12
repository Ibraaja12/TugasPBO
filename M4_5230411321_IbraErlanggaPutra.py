import uuid

class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.id = str(uuid.uuid4())
        self.nama = nama
        self.ktp = ktp
        self.limit_pinjaman = limit_pinjaman
        self.transaksi = []

    def __str__(self):
        return f"Debitur {self.nama} (KTP: {self.ktp})"

class DatabaseDebitur:
    def __init__(self):
        self.debitur_list = []
        self.ktp_list = set()

    def tambah_debitur(self, debitur):
        if debitur.ktp in self.ktp_list:
            raise ValueError(f"Nomor KTP {debitur.ktp} sudah terdaftar")
        self.debitur_list.append(debitur)
        self.ktp_list.add(debitur.ktp)
        print(f"Debitur {debitur} berhasil ditambahkan.")

    def get_debitur_by_ktp(self, ktp):
        for debitur in self.debitur_list:
            if debitur.ktp == ktp:
                return debitur
        return None

    def get_all_debiturs(self):
        return self.debitur_list

    def tambah_pinjaman(self, nama, jumlah_pinjaman):
        for debitur in self.debitur_list:
            if debitur.nama == nama:
                if jumlah_pinjaman > debitur.limit_pinjaman:
                    print(f"Error: Pinjaman {jumlah_pinjaman} melebihi limit {debitur.limit_pinjaman} untuk Debitur {debitur.nama}")
                    return
                debitur.transaksi.append({"jenis": "pinjaman", "jumlah": jumlah_pinjaman})
                print(f"Pinjaman {jumlah_pinjaman} berhasil ditambahkan untuk Debitur {debitur.nama}")
                return
        print(f"Error: Debitur {nama} tidak ditemukan")

    def tampilkan_pinjaman(self, nama):
        for debitur in self.debitur_list:
            if debitur.nama == nama:
                for transaksi in debitur.transaksi:
                    if transaksi["jenis"] == "pinjaman":
                        jumlah_pinjaman = transaksi["jumlah"]
                        bunga = 0.05  # bunga (/bulan)
                        bulan = 12  # tenor keterlambatan
                        angsuran = jumlah_pinjaman * (1 + bunga) ** (1 / bulan)
                        print(f"Pinjaman untuk Debitur {debitur.nama}:")
                        print(f"  Jumlah Pinjaman: {jumlah_pinjaman}")
                        print(f"  Bunga: {bunga * 100}%")
                        print(f"  Jangka Waktu: {bulan} bulan")
                        print(f"  Angsuran per Bulan: {angsuran:.2f}")
                        return
        print(f"Error: Debitur {nama} tidak ditemukan atau tidak memiliki pinjaman")

db = DatabaseDebitur()

while True:
    print("Menu:")
    print("1. Tambah Debitur")
    print("2. Tambah Pinjaman")
    print("3. Tampilkan Pinjaman")
    print("4. Keluar")
    choice = input("Pilih menu: ")

    if choice == "1":
        nama = input("Masukkan nama debitur: ")
        ktp = input("Masukkan nomor KTP: ")
        limit_pinjaman = int(input("Masukkan limit pinjaman: "))
        db.tambah_debitur(Debitur(nama, ktp, limit_pinjaman))
    elif choice == "2":
        nama = input("Masukkan nama debitur: ")
        jumlah_pinjaman = int(input("Masukkan jumlah pinjaman: "))
        db.tambah_pinjaman(nama, jumlah_pinjaman)
    elif choice == "3":
        nama = input("Masukkan nama debitur: ")
        db.tampilkan_pinjaman(nama)
    elif choice == "4":
        break
    else:
        print("Menu tidak valid. Silakan coba lagi.")