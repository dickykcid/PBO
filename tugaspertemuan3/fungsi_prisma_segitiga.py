import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W

def hitung_luas(txtpanjangalas, txttinggialas, txttinggiprisma):
    panjangalas = float(txtpanjangalas)
    tinggialas = float(txttinggialas)
    tinggiprisma = float(txttinggiprisma)
    luas = tinggiprisma*(3*panjangalas)+(2*((1/2)*panjangalas*tinggialas))
    return luas

def hitung_volume(txtpanjangalas, txttinggialas, txttinggiprisma):
    panjangalas = float(txtpanjangalas)
    tinggialas = float(txttinggialas)
    tinggiprisma = float(txttinggiprisma)
    volume = ((1/2)*panjangalas*tinggialas)*tinggiprisma
    return volume
