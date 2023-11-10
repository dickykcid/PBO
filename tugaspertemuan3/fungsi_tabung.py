import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W
from math import pi

def hitung_luas(txtjarijari, txttinggitabung):
    r = float(txtjarijari)
    tinggitabung = float(txttinggitabung)
    luas = (2*pi*r*tinggitabung)+(2*pi*r*r)
    return luas

def hitung_volume(txtjarijari, txttinggitabung):
    r = float(txtjarijari)
    tinggitabung = float(txttinggitabung)
    volume = pi*r*r*tinggitabung
    return volume