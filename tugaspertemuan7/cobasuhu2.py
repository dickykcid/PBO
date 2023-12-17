import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W
from math import pi

def celcius_ke_kelvin(txtsuhu):
    celcius_kelvin = float(txtsuhu)
    konversi_celcius_kelvin = 
    return 

def hitung_volume(txtjarijari):
    r = float(txtjarijari)
    volume = (4/3)*pi*r*r*r
    return volume

app = Tk()

app.title("Kalkulator Konversi Suhu")

frame = Frame(app)
frame.pack(padx=40, pady=40)


r = Label(frame, text="RJARI-JARI :")
r.grid(row=1, column=0, sticky=W, padx=5, pady=5)
 
txtjarijari = Entry(frame)
txtjarijari.grid(row=2, column=0, sticky=W, padx=5, pady=5)


def hitung():
    hasil_luas = hitung_luas(txtjarijari.get())
    hasil_volume = hitung_volume(txtjarijari.get())
    txtluas.delete(0, END)
    txtluas.insert(END, hasil_luas)
    txtvolume.delete(0, END)
    txtvolume.insert(END, hasil_volume)
hitung_button = Button(frame, text="HITUNG ", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#label luas
luas = Label(frame, text="LUAS : ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#textbook luas
txtluas = Entry(frame)
txtluas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

#label volume
volume = Label(frame, text="VOLUME :")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

#textbook volume
txtvolume = Entry(frame)
txtvolume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

#label nama
nama = Label(frame, text="DICKY FRANSSETIAJI - 231511010 - TI22L")
nama.grid(row=8, column=0, sticky=W, padx=5, pady=5)

app.mainloop()