import tkinter as tk
from tkinter import messagebox
import time
import random

# Kelas utama aplikasi
class StudentProductivityToolkit:
    def __init__(self, root):

        # Pengaturan jendela utama
        self.root = root
        self.root.title("Student Productivity Toolkit")
        self.root.geometry("400x500")

        # Judul Aplikasi
        judul = tk.Label(root, text="Student Productivity Toolkit", font=("Arial", 18))
        judul.pack(pady=20)

        # Tombol - tombol fitur
        tombol_timer = tk.Button(root, text="Timer Belajar", command=self.timer_belajar, width=26)
        tombol_timer.pack(pady=10)

        tombol_catatan = tk.Button(root, text="Catatan Harian", command=self.membuat_catatan_harian, width=26)
        tombol_catatan.pack(pady=10)

        tombol_tugas = tk.Button(root, text="To-Do List", command=self.buka_to_do_list, width=26)
        tombol_tugas.pack(pady=10)

        tombol_kalkulator = tk.Button(root, text="Kalkulator Sederhana", command=self.buka_kalkulator, width=26)
        tombol_kalkulator.pack(pady=10)

        tombol_motivasi = tk.Button(root, text="Motivational Quote Generator", command=self.tampilkan_motivasi, width=26)
        tombol_motivasi.pack(pady=10)

    # Mendefinisikan fungsi timer_belajar
    def timer_belajar(self):
        # Jendela Timer Belajar
        jendela_timer = tk.Toplevel(self.root)
        jendela_timer.title("Timer Belajar")
        jendela_timer.geometry("300x200")

        # Label waktu
        label_waktu = tk.Label(jendela_timer, text="00:00", font=("Arial", 25))
        label_waktu.pack(pady=20)

        # Input durasi
        label_durasi = tk.Label(jendela_timer, text="Masukkan durasi (menit):")
        label_durasi.pack()
        input_durasi = tk.Entry(jendela_timer)
        input_durasi.pack()

        def mulai_timer():
            try:
                # Durasi dari input
                menit = int(input_durasi.get())
                detik = menit * 60

                # Hitung mundur
                def hitung_mundur():
                    nonlocal detik
                    if detik > 0:
                        menit_tampil = detik // 60
                        detik_tampil = detik % 60
                        label_waktu.config(text=f"{menit_tampil:02d}:{detik_tampil:02d}")
                        detik -= 1
                        jendela_timer.after(1000, hitung_mundur)
                    else:
                        messagebox.showinfo("Selesai", "Waktu belajar telah habis!")
                hitung_mundur() # Mulai hitung mundur

            except ValueError:
                messagebox.showerror("Error", "Masukkan durasi yang valid!")

        # Tombol mulai
        tombol_mulai = tk.Button(jendela_timer, text="Mulai", command=mulai_timer)
        tombol_mulai.pack(pady=12)

    # Mendefinisikan fungsi catatan_harian
    def membuat_catatan_harian(self):
        # Jendela Catatan Harian
        jendela_catatan = tk.Toplevel(self.root)
        jendela_catatan.title("Catatan Harian")
        jendela_catatan.geometry("400x300")

        # Area teks
        area_catatan = tk.Text(jendela_catatan, height=10)
        area_catatan.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        def simpan_catatan():
            # Simpan catatan ke file
            with open("catatan_harian.txt", "w") as file:
                file.write(area_catatan.get("1.0", tk.END))
            messagebox.showinfo("Berhasil", "Catatan telah disimpan!")

        # Tombol simpan
        tombol_simpan = tk.Button(jendela_catatan, text="Simpan", command=simpan_catatan)
        tombol_simpan.pack(pady=12)

    # Mendefinisikan fungsi todo_list
    def buka_to_do_list(self):
        # Jendela Daftar Tugas
        jendela_tugas = tk.Toplevel(self.root)
        jendela_tugas.title("Daftar Tugas")
        jendela_tugas.geometry("300x400")

        # Daftar tugas
        daftar_tugas = tk.Listbox(jendela_tugas)
        daftar_tugas.pack(padx=12, pady=12, expand=True, fill=tk.BOTH)

        # Input tugas
        input_tugas = tk.Entry(jendela_tugas)
        input_tugas.pack(padx=12)

         # Tambah tugas 
        def tambah_list():
            tugas = input_tugas.get()
            if tugas:
                daftar_tugas.insert(tk.END, tugas)
                input_tugas.delete(0, tk.END)

        # Hapus tugas 
        def hapus_list():
            try:
                index = daftar_tugas.curselection()[0]
                daftar_tugas.delete(index)
            except:
                messagebox.showwarning("Peringatan!", "Pilih tugas yang akan dihapus")

        # Tombol tambah dan hapus
        tombol_tambah = tk.Button(jendela_tugas, text="Tambah Tugas", command=tambah_list)
        tombol_tambah.pack(side=tk.LEFT, padx=12, pady=12)

        tombol_hapus = tk.Button(jendela_tugas, text="Hapus Tugas", command=hapus_list)
        tombol_hapus.pack(side=tk.RIGHT, padx=12, pady=12)

    # Fungsi kalkulator
    
    def buka_kalkulator(self):
        # Jendela Kalkulator
        jendela_kalkulator = tk.Toplevel(self.root)
        jendela_kalkulator.title("Kalkulator Sederhana")
        jendela_kalkulator.geometry("300x400")

        # Layar kalkulator
        layar = tk.Entry(jendela_kalkulator, width=20, justify='right')
        layar.grid(row=0, column=0, columnspan=5, padx=6, pady=6)

        # Fungsi tombol
        def klik_tombol(angka):
            sekarang = layar.get()
            layar.delete(0, tk.END)
            layar.insert(0, sekarang + str(angka))

        def hitung():
            try:
                hasil = eval(layar.get())
                layar.delete(0, tk.END)
                layar.insert(0, hasil)
            except:
                layar.delete(0, tk.END)
                layar.insert(0, "Error")

        def bersihkan():
            layar.delete(0, tk.END)

        # Tombol-tombol
        tombol = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Buat tombol
        baris = 1
        kolom = 0
        for tombol_val in tombol:
            if tombol_val == '=':
                tk.Button(jendela_kalkulator, text=tombol_val, 
                          command=hitung).grid(row=baris, column=kolom)
            else:
                tk.Button(jendela_kalkulator, text=tombol_val, 
                          command=lambda x=tombol_val: klik_tombol(x)).grid(row=baris, column=kolom)
            
            kolom += 1
            if kolom > 3:
                kolom = 0
                baris += 1

    # Fungsi motivasi
    def tampilkan_motivasi(self):
        # Kata-Kata Motivasi
        motivasi = [
            "Kamu lebih kuat dari semua rintangan yang terlihat sulit, teruslah melangkah, dan kamu akan sampai.",
            "Apa yang kamu perjuangkan hari ini akan menjadi cerita keberhasilanmu di masa depan.",
            "Jika kamu merasa lelah, istirahatlah, tapi jangan pernah berhenti melangkah.",
            "Tantangan ada bukan untuk menjatuhkanmu, tapi untuk membuatmu lebih kuat dan tangguh.",
            "Kamu tidak sendirian, setiap orang hebat pernah memulai dari nol."
        ]
        # Tampilkan motivasi secara acak
        pesan_motivasi = random.choice(motivasi)
        messagebox.showinfo("Motivasi Hari Ini", pesan_motivasi)

# Fungsi utama untuk menjalankan aplikasi
def main():
    # Buat jendela utama
    root = tk.Tk()
    
    # Inisiasi aplikasi
    aplikasi = StudentProductivityToolkit(root)
    
    # Jalankan aplikasi
    root.mainloop()

# Jalankan program
if __name__ == "__main__":
    main()