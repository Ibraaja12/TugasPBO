class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def tampilkan_info(self):
        print(f"Judul: {self.judul}, Penyanyi: {self.penyanyi}, Genre: {self.genre}")

class Pop(Music):
    def __init__(self, judul, penyanyi):
        super().__init__(judul, penyanyi, "Pop")

class Rock(Music):
    def __init__(self, judul, penyanyi):
        super().__init__(judul, penyanyi, "Rock")

class Jazz(Music):
    def __init__(self, judul, penyanyi):
        super().__init__(judul, penyanyi, "Jazz")

class Playlist:
    def __init__(self):
        self.musics = []

    def add_music(self, music):
        if isinstance(music, Music):
            self.musics.append(music)
            print(f"Lagu '{music.judul}' ditambahkan.")
        else:
            print("Objek yang ditambahkan bukan merupakan musik yang valid.")

    def delete_music(self, judul):
        for music in self.musics:
            if music.judul.lower() == judul.lower():
                self.musics.remove(music)
                print(f"Lagu '{judul}' dihapus.")
                return
        print(f"Lagu '{judul}' tidak ditemukan.")

    def display_musics(self):
        if not self.musics:
            print("Tidak ada musik dalam playlist.")
        else:
            print("Daftar Musik:")
            for music in self.musics:
                music.tampilkan_info()

    def sort_musics(self):
        self.musics.sort(key=lambda music: music.judul)
        print("Playlist diurutkan berdasarkan judul (A-Z).")

    def cari_penyanyi(self, penyanyi):
        hasil = [music for music in self.musics if penyanyi.lower() in music.penyanyi.lower()]
        if hasil:
            print(f"Musik oleh '{penyanyi}':")
            for music in hasil:
                music.tampilkan_info()
        else:
            print(f"Tidak ada musik oleh '{penyanyi}'.")

    def cari_judul(self, judul):
        hasil = [music for music in self.musics if judul.lower() in music.judul.lower()]
        if hasil:
            print(f"Musik dengan judul '{judul}':")
            for music in hasil:
                music.tampilkan_info()
        else:
            print(f"Tidak ada musik dengan judul '{judul}'.")

    def clear_playlist(self):
        self.musics.clear()
        print("Playlist telah dibersihkan.")

def input_music_data():
    judul = input("Masukkan judul musik: ")
    penyanyi = input("Masukkan penyanyi musik: ")
    genre = input("Masukkan genre musik (Pop, Rock, Jazz): ").lower()
    return judul, penyanyi, genre

def main():
    playlist = Playlist()

    while True:
        print("\nMenu Playlist Musik:")
        print("1. Tambah Musik")
        print("2. Hapus Musik")
        print("3. Tampilkan Musik")
        print("4. Urutkan Musik")
        print("5. Cari Musik oleh Penyanyi")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul, penyanyi, genre = input_music_data()
            if genre == "pop":
                playlist.add_music(Pop(judul, penyanyi))
            elif genre == "rock":
                playlist.add_music(Rock(judul, penyanyi))
            elif genre == "jazz":
                playlist.add_music(Jazz(judul, penyanyi))
            else:
                print("Genre musik tidak valid.")

        elif pilihan == "2":
            judul = input("Masukkan judul musik yang ingin dihapus: ")
            playlist.delete_music(judul)

        elif pilihan == "3":
            playlist.display_musics()

        elif pilihan == "4":
            playlist.sort_musics()

        elif pilihan == "5":
            penyanyi = input("Masukkan penyanyi musik yang ingin dicari: ")
            playlist.cari_penyanyi(penyanyi)


        elif pilihan == "6":
            print("Keluar dari aplikasi. Terima kasih, Selamat Mendengarkan!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
