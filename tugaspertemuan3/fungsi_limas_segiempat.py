import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W

def hitung_luas(txtpanjangalas, txttinggiselimut):
    panjangalas = float(txtpanjangalas)
    tinggiselimut = float(txttinggiselimut)
    luas = (panjangalas*panjangalas)+(4*((1/2)*panjangalas*tinggiselimut))
    return luas

def hitung_volume(txtpanjangalas, txttinggilimas):
    panjangalas = float(txtpanjangalas)
    tinggilimas = float(txttinggilimas)
    volume = (1/3)*(panjangalas*panjangalas)*tinggilimas
    return volume