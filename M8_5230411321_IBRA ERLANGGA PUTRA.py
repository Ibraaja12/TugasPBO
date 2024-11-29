import tkinter as tk
from tkinter import ttk, messagebox

class MountainGearRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Persewaan Peralatan Gunung")
        self.root.geometry("500x500")

        self.rentals = []  # List untuk menyimpan data persewaan

        self.create_widgets()

    def create_widgets(self):
        # Judul Aplikasi
        title_label = tk.Label(self.root, text="Aplikasi Persewaan Peralatan Gunung", font=("Arial", 16))
        title_label.pack(pady=10)

        # Nama Penyewa
        name_label = tk.Label(self.root, text="Nama Penyewa:")
        name_label.pack()
        self.name_entry = tk.Entry(self.root, width=35)
        self.name_entry.pack(pady=5)

        # Pilihan Peralatan
        gear_label = tk.Label(self.root, text="Pilih Peralatan:")
        gear_label.pack()
        self.gear_option = ttk.Combobox(self.root, values=("Tenda", "Sleeping Bag", "Carrier", "Kompor Portable", "Matras", "Trekking Pole"))
        self.gear_option.pack(pady=5)

        # Lama Sewa (hari)
        duration_label = tk.Label(self.root, text="Lama Sewa (hari):")
        duration_label.pack()
        self.duration_entry = tk.Entry(self.root, width=10)
        self.duration_entry.pack(pady=5)

        # Button untuk menyewa peralatan
        rent_button = tk.Button(self.root, text="Sewa", command=self.submit_rental)
        rent_button.pack(pady=10)

        # Button untuk menghapus persewaan
        delete_button = tk.Button(self.root, text="Hapus Persewaan", command=self.delete_rental)
        delete_button.pack(pady=5)

        # Button untuk menghapus semua persewaan
        delete_all_button = tk.Button(self.root, text="Hapus Semua Persewaan", command=self.delete_all_rentals)
        delete_all_button.pack(pady=5)

        # Tabel Daftar Persewaan
        self.rental_tree = ttk.Treeview(self.root, columns=("Nama", "Peralatan", "Lama"), show='headings')
        self.rental_tree.heading("Nama", text="Nama Penyewa")
        self.rental_tree.heading("Peralatan", text="Peralatan")
        self.rental_tree.heading("Lama", text="Lama Sewa (hari)")
        self.rental_tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar untuk tabel
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.rental_tree.yview)
        self.rental_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

    def submit_rental(self):
        name = self.name_entry.get().strip()
        gear = self.gear_option.get()
        duration = self.duration_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Nama Penyewa tidak boleh kosong!")
            return

        if not gear:
            messagebox.showerror("Error", "Silakan pilih peralatan!")
            return

        if not duration.isdigit() or int(duration) <= 0:
            messagebox.showerror("Error", "Lama sewa harus berupa angka positif!")
            return

        # Menambahkan data persewaan ke daftar
        self.rentals.append((name, gear, duration))
        self.update_rental_table()

        # Menghapus input setelah penyewaan
        self.name_entry.delete(0, tk.END)
        self.gear_option.set('')
        self.duration_entry.delete(0, tk.END)

    def update_rental_table(self):
        # Menghapus semua item di tabel
        for item in self.rental_tree.get_children():
            self.rental_tree.delete(item)

        # Menambahkan semua persewaan ke tabel
        for rental in self.rentals:
            self.rental_tree.insert("", "end", values=rental)

    def delete_rental(self):
        selected_item = self.rental_tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Silakan pilih persewaan yang ingin dihapus!")
            return

        # Menghapus persewaan dari daftar
        for item in selected_item:
            values = self.rental_tree.item(item, "values")
            self.rentals.remove(values)
            self.rental_tree.delete(item)

        messagebox.showinfo("Informasi", "Persewaan berhasil dihapus!")

    def delete_all_rentals(self):
        # Menghapus semua persewaan
        self.rentals.clear()
        self.update_rental_table()
        messagebox.showinfo("Informasi", "Semua persewaan berhasil dihapus!")

if __name__ == '__main__':
    root = tk.Tk()
    app = MountainGearRentalApp(root)
    root.mainloop()
