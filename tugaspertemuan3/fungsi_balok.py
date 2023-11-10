import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W

def hitung_luas(txtpanjang, txtlebar, txttinggi):
    panjang = float(txtpanjang)
    lebar = float(txtlebar)
    tinggi = float(txttinggi)
    luas = (2*panjang*lebar)+(2*panjang*tinggi)+(2*lebar*tinggi)
    return luas

def hitung_volume(txtpanjang, txtlebar, txttinggi):
    panjang = float(txtpanjang)
    lebar = float(txtlebar)
    tinggi = float(txttinggi)
    volume = panjang * lebar * tinggi
    return volume
