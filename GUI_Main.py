import tkinter as tk
from tkinter import filedialog, messagebox
from teskode import bagi_kelompok
from CekDouble import cek_duplikat_nim
from PIL import Image, ImageTk

def jalankan_pembagian():
    file_path = filedialog.askopenfilename(title="Pilih File Excel Input")
    if file_path:
        try:
            output_file = bagi_kelompok(file_path, 130)
            messagebox.showinfo("Sukses", f"Pembagian berhasil!\nFile output:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def jalankan_cek_duplikat():
    file_path = filedialog.askopenfilename(title="Pilih File Excel Hasil Kelompok")
    if file_path:
        try:
            duplikat = cek_duplikat_nim(file_path)
            if not duplikat.empty:
                messagebox.showwarning("Duplikat Ditemukan", duplikat.to_string())
            else:
                messagebox.showinfo("Aman", "Tidak ada NIM duplikat.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Aplikasi Kelompok MABA")
root.geometry("600x300")
root.resizable(False, False)

frame_kiri = tk.Frame(root, bg="#7A8B81")
frame_kiri.pack(side="left", fill="both", expand=True)

img = Image.open("Logo_UPNVJ.png")
img = img.resize((150, 150))  
logo_img = ImageTk.PhotoImage(img)

logo = tk.Label(frame_kiri, image=logo_img, bg="#7A8B81")
logo.image = logo_img
logo.pack(pady=(40, 10))


label_desc = tk.Label(frame_kiri, text="Pembagi Data MABA", font=("Helvetica", 14), bg="#7A8B81", fg="white")
label_desc.pack()

frame_kanan = tk.Frame(root, bg="white")
frame_kanan.pack(side="right", fill="both", expand=True)

judul = tk.Label(frame_kanan, text="Menu Aplikasi", font=("Helvetica", 14), bg="white")
judul.pack(pady=(40, 20))

btn1 = tk.Button(frame_kanan, text="1. Bagi Kelompok", command=jalankan_pembagian, width=25)
btn1.pack(pady=5)

btn2 = tk.Button(frame_kanan, text="2. Cek Duplikat NIM", command=jalankan_cek_duplikat, width=25)
btn2.pack(pady=5)

root.mainloop()
