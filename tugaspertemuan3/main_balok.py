import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W
from fungsi_balok import hitung_luas, hitung_volume

app = Tk()

app.title("Kalkulator Luas dan Volume Balok")

frame = Frame(app)
frame.pack(padx=40, pady=40)


#label panjang
panjang = Label(frame, text="PANJANG :")
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)
 

#textbook panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#label lebar
lebar = Label(frame, text="LEBAR :")
lebar.grid(row=3, column=0, sticky=W, padx=5, pady=5)
 
#textbook lebar
txtlebar = Entry(frame)
txtlebar.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#label tinggi
tinggi = Label(frame, text="TINGGI :")
tinggi.grid(row=5, column=0, sticky=W, padx=5, pady=5)
 
#textbook tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=6, column=0, sticky=W, padx=5, pady=5)

#button
def hitung():
    hasil_luas = hitung_luas(txtpanjang.get(), txtlebar.get(), txttinggi.get())
    hasil_volume = hitung_volume(txtpanjang.get(), txtlebar.get(), txttinggi.get())
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