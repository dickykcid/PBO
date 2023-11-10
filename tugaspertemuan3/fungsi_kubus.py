import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W

def hitung_luas(txtrusuk):
    R = float(txtrusuk)
    luas = 6 * R * R
    return luas

def hitung_volume(txtrusuk):
    R = float(txtrusuk)
    volume = R * R * R
    return volume
