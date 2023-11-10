import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W
from fungsi_limas_segitiga import hitung_luas, hitung_volume

app = Tk()

app.title("Kalkulator Luas dan Volume Limas Segitiga")

frame = Frame(app)
frame.pack(padx=40, pady=40)


panjangalas = Label(frame, text="PANJANG ALAS :")
panjangalas.grid(row=1, column=0, sticky=W, padx=5, pady=5)
 
txtpanjangalas = Entry(frame)
txtpanjangalas.grid(row=2, column=0, sticky=W, padx=5, pady=5)


tinggialas = Label(frame, text="TINGGI ALAS :")
tinggialas.grid(row=3, column=0, sticky=W, padx=5, pady=5)
 
txttinggialas = Entry(frame)
txttinggialas.grid(row=4, column=0, sticky=W, padx=5, pady=5)


tinggiselimut = Label(frame, text="TINGGI SELIMUT :")
tinggiselimut.grid(row=5, column=0, sticky=W, padx=5, pady=5)
 
txttinggiselimut = Entry(frame)
txttinggiselimut.grid(row=6, column=0, sticky=W, padx=5, pady=5)

tinggilimas = Label(frame, text="TINGGI LIMAS :")
tinggilimas.grid(row=7, column=0, sticky=W, padx=5, pady=5)
 
txttinggilimas = Entry(frame)
txttinggilimas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

#button
def hitung():
    hasil_luas = hitung_luas(txtpanjangalas.get(), txttinggialas.get(), txttinggiselimut.get())
    hasil_volume = hitung_volume(txtpanjangalas.get(), txttinggialas.get(), txttinggilimas.get())
    txtluas.delete(0, END)
    txtluas.insert(END, hasil_luas)
    txtvolume.delete(0, END)
    txtvolume.insert(END, hasil_volume)
hitung_button = Button(frame, text="HITUNG ", command=hitung)
hitung_button.grid(row=9, column=0, sticky=W, padx=5, pady=5)

luas = Label(frame, text="LUAS : ")
luas.grid(row=10, column=0, sticky=W, padx=5, pady=5)

txtluas = Entry(frame)
txtluas.grid(row=11, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="VOLUME :")
volume.grid(row=12, column=0, sticky=W, padx=5, pady=5)

txtvolume = Entry(frame)
txtvolume.grid(row=13, column=0, sticky=W, padx=5, pady=5)

nama = Label(frame, text="DICKY FRANSSETIAJI - 231511010 - TI22L")
nama.grid(row=14, column=0, sticky=W, padx=5, pady=5)
app.mainloop()