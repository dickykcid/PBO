import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W
from fungsi_kerucut import hitung_luas, hitung_volume

app = Tk()

app.title("Kalkulator Luas dan Volume Kerucut")

frame = Frame(app)
frame.pack(padx=40, pady=40)


r = Label(frame, text="JARI-JARI :")
r.grid(row=1, column=0, sticky=W, padx=5, pady=5)
 
txtjarijari = Entry(frame)
txtjarijari.grid(row=2, column=0, sticky=W, padx=5, pady=5)


tinggiselimut = Label(frame, text="TINGGI SELIMUT :")
tinggiselimut.grid(row=3, column=0, sticky=W, padx=5, pady=5)
 
txttinggiselimut = Entry(frame)
txttinggiselimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)

tinggikerucut = Label(frame, text="TINGGI KERUCUT :")
tinggikerucut.grid(row=5, column=0, sticky=W, padx=5, pady=5)
 
txttinggikerucut = Entry(frame)
txttinggikerucut.grid(row=6, column=0, sticky=W, padx=5, pady=5)

#button
def hitung():
    hasil_luas = hitung_luas(txtjarijari.get(), txttinggiselimut.get())
    hasil_volume = hitung_volume(txtjarijari.get(), txttinggikerucut.get())
    txtluas.delete(0, END)
    txtluas.insert(END, hasil_luas)
    txtvolume.delete(0, END)
    txtvolume.insert(END, hasil_volume)
hitung_button = Button(frame, text="HITUNG ", command=hitung)
hitung_button.grid(row=7, column=0, sticky=W, padx=5, pady=5)

luas = Label(frame, text="LUAS : ")
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

txtluas = Entry(frame)
txtluas.grid(row=9, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="VOLUME :")
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

txtvolume = Entry(frame)
txtvolume.grid(row=11, column=0, sticky=W, padx=5, pady=5)

nama = Label(frame, text="DICKY FRANSSETIAJI - 231511010 - TI22L")
nama.grid(row=12, column=0, sticky=W, padx=5, pady=5)
app.mainloop()