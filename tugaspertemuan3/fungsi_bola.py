import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W
from math import pi

def hitung_luas(txtjarijari):
    r = float(txtjarijari)
    luas = 4*pi*r*r
    return luas

def hitung_volume(txtjarijari):
    r = float(txtjarijari)
    volume = (4/3)*pi*r*r*r
    return volume