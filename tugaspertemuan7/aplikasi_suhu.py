# Import modul tkinter dengan alias 'tk'
import tkinter as tk
# Import modul ttk dari tkinter
from tkinter import ttk

# Fungsi untuk melakukan konversi suhu
def konversi():
    try:
        # Mengambil nilai dari suhu dan mengubahnya menjadi float
        nilai_suhu= float(suhu.get())
        # Mengambil satuan suhu yang dipilih dari combobox satuan suhu
        satuan_suhu = combobox_satuan_suhu.get()
        # Mengambil satuan suhu yang dipilih dari combobox output
        konversi_satuan_suhu = combobox_konversi_suhu.get()

        # Jika pilihan satuan suhu dan konversi satuan adalah jenis suhu yang sama :
        if satuan_suhu == konversi_satuan_suhu:
            variabel_hasil_konversi.set(f"{nilai_suhu} {satuan_suhu} = {nilai_suhu} {konversi_satuan_suhu}")

        # Jika pilihan satuan suhu adalah celcius dan konversi satuan adalah fahrenheit :
        elif satuan_suhu == "Celsius" and konversi_satuan_suhu == "Fahrenheit":
            hasil_konversi = (nilai_suhu* 9/5) + 32
            variabel_hasil_konversi.set(f"{nilai_suhu} Celsius = {hasil_konversi:.2f} Fahrenheit")

        # Jika pilihan satuan suhu adalah fahrenheit dan konversi satuan adalah celcius :      
        elif satuan_suhu == "Fahrenheit" and konversi_satuan_suhu == "Celsius":
            hasil_konversi = (nilai_suhu- 32) * 5/9
            variabel_hasil_konversi.set(f"{nilai_suhu} Fahrenheit = {hasil_konversi:.2f} Celsius")

        # Jika pilihan satuan suhu adalah celcius dan konversi satuan adalah kelvin :      
        elif satuan_suhu == "Celsius" and konversi_satuan_suhu == "Kelvin":
            hasil_konversi = nilai_suhu+ 273.15
            variabel_hasil_konversi.set(f"{nilai_suhu} Celsius = {hasil_konversi:.2f} Kelvin")

        # Jika pilihan satuan suhu adalah kelvin dan konversi satuan adalah celcius :      
        elif satuan_suhu == "Kelvin" and konversi_satuan_suhu == "Celsius":
            hasil_konversi = nilai_suhu- 273.15
            variabel_hasil_konversi.set(f"{nilai_suhu} Kelvin = {hasil_konversi:.2f} Celsius")

        # Jika pilihan satuan suhu adalah fahrenheit dan konversi satuan adalah kelvin :      
        elif satuan_suhu == "Fahrenheit" and konversi_satuan_suhu == "Kelvin":
            celsius = (nilai_suhu- 32) * 5/9
            hasil_konversi = celsius + 273.15
            variabel_hasil_konversi.set(f"{nilai_suhu} Fahrenheit = {hasil_konversi:.2f} Kelvin")

        # Jika pilihan satuan suhu adalah kelvin dan konversi satuan adalah fahrenheit :      
        elif satuan_suhu == "Kelvin" and konversi_satuan_suhu == "Fahrenheit":
            celsius = nilai_suhu- 273.15
            hasil_konversi = (celsius * 9/5) + 32
            variabel_hasil_konversi.set(f"{nilai_suhu} Kelvin = {hasil_konversi:.2f} Fahrenheit")
        

    # Menangani exception jika nilai yang dimasukkan tidak valid
    except ValueError :
        variabel_hasil_konversi.set("Error: Masukan bukan angka")

# Membuat instance dari Tkinter
root = tk.Tk()
# Memberi judul pada windows
root.title("Konverter Suhu")

# Membuat label untuk input suhu
label_input = tk.Label(root, text="Masukkan suhu:")
label_input.pack(pady=10)

# Membuat entry widget untuk memasukkan suhu
suhu = tk.Entry(root)
suhu.pack(pady=10)

# Membuat label untuk satuan suhu pada input
label_input_unit = tk.Label(root, text="Satuan suhu:")
label_input_unit.pack(pady=10)

# Membuat combobox untuk memilih satuan suhu pada input
combobox_satuan_suhu = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
combobox_satuan_suhu.pack(pady=10)
combobox_satuan_suhu.set("Celsius")

# Membuat label untuk satuan suhu pada output
label_output_unit = tk.Label(root, text="Konversi ke satuan:")
label_output_unit.pack(pady=10)

# Membuat combobox untuk memilih satuan suhu pada output
combobox_konversi_suhu = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
combobox_konversi_suhu.pack(pady=10)
combobox_konversi_suhu.set("Fahrenheit")

# Membuat tombol untuk melakukan konversi
tombol_konversi = tk.Button(root, text="Konversi", command=konversi)
tombol_konversi.pack(pady=10)

# Variabel StringVar untuk menampilkan hasil konversi pada label
variabel_hasil_konversi = tk.StringVar()
# Membuat label untuk menampilkan hasil konversi
label_hasil_konversi = tk.Label(root, textvariable = variabel_hasil_konversi)
label_hasil_konversi.pack(pady=10)

# Memulai main loop Tkinter
root.mainloop()
