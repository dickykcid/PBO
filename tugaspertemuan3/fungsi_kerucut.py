import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W
from math import pi

def hitung_luas(txtjarijari, txttinggiselimut):
    r = float(txtjarijari)
    tinggiselimut = float(txttinggiselimut)
    luas = (pi*r*tinggiselimut)+(pi*r*r)
    return luas

def hitung_volume(txtjarijari, txttinggikerucut):
    r = float(txtjarijari)
    tinggikerucut = float(txttinggikerucut)
    volume = (1/3)*pi*r*r*tinggikerucut
    return volume