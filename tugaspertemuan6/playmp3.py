import tkinter as tk
from pygame import mixer

# Fungsi untuk memutar MP3 menggunakan modul pygame mixer yang lebih ringan
def play_music():
    mixer.init()
    # Memuat file MP3 ke dalam mixer
    mixer.music.load("E:/UMC/TUGAS SEMESTER GANJIL/PBO/tugaspertemuan6/NyanCat.mp3")
    # Memainkan musik
    mixer.music.play()
 
# Fungsi untuk menghentikan musik
def stop_music():
    mixer.music.stop()

# Membuat GUI
root = tk.Tk()
root.title("MP3 Player")

# Button untuk memutar file MP3, dengan perintah yang mengarah ke fungsi play_music
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=10)

# Button untuk menghentikan musik, dengan perintah yang mengarah ke fungsi stop_music
stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

# Menjalankan loop GUI
root.mainloop()


