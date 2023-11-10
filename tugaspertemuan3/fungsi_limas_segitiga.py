import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W

def hitung_luas(txtpanjangalas, txttinggialas, txttinggiselimut):
    panjangalas = float(txtpanjangalas)
    tinggialas = float(txttinggialas)
    tinggiselimut = float(txttinggiselimut)
    luas = ((1/2)*(panjangalas*tinggialas))+(3*((1/2)*panjangalas*tinggiselimut))
    return luas

def hitung_volume(txtpanjangalas, txttinggialas, txttinggilimas):
    panjangalas = float(txtpanjangalas)
    tinggialas = float(txttinggialas)
    tinggilimas = float(txttinggilimas)
    volume = (1/3)*((1/2)*panjangalas*tinggialas)*tinggilimas
    return volume
