import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk

# Inisialisasi variabel global
cap = None

# Fungsi untuk memutar video
def play_video():
    global cap
    # Membuka file video menggunakan cv2.VideoCapture
    cap = cv2.VideoCapture("E:/UMC/TUGAS SEMESTER GANJIL/PBO/tugaspertemuan6/NyanCat.mp4")
    # Menampilkan frame-video dalam jendela Tkinter
    show_frame()

# Fungsi untuk menampilkan frame video dalam jendela Tkinter
def show_frame():
    global cap
    # Membaca frame dari objek VideoCapture
    ret, frame = cap.read()
    if ret:
        # Konversi frame dari BGR ke RGB untuk Tkinter
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Konversi frame ke format gambar Tkinter
        img = Image.fromarray(rgb_frame)
        img = ImageTk.PhotoImage(image=img)

        # Menampilkan gambar dalam label Tkinter
        video_label.config(image=img)
        video_label.image = img

        # Mengeksekusi fungsi show_frame setiap 25 milidetik
        root.after(25, show_frame)
    else:
        # Memanggil fungsi untuk menghentikan video
        stop_video()

# Fungsi untuk menghentikan video
def stop_video():
    global cap
    if cap is not None:
        cap.release()
        video_label.config(image=None)

# Membuat GUI
root = tk.Tk()
root.title("Video Player")

# Button untuk memutar file video MP4
play_button = tk.Button(root, text="Play", command=play_video)
play_button.pack(pady=10)

# Label untuk menampilkan video
video_label = tk.Label(root)
video_label.pack(pady=10)

# Button untuk menghentikan video
stop_button = tk.Button(root, text="Stop", command=stop_video)
stop_button.pack(pady=10)

root.mainloop()