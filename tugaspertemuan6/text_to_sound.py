import tkinter as tk
from gtts import gTTS
from playsound import playsound

# Fungsi untuk mengonversi teks ke suara
def text_to_speech():
    input_text = text_entry.get()  # Mendapatkan teks dari input pengguna

    if input_text:
        # Menggunakan gTTS untuk mengonversi teks menjadi suara dengan bahasa Indonesia ('id')
        tts = gTTS(text=input_text, lang='id', slow=False)
        tts.save('E:/UMC/TUGAS SEMESTER GANJIL/PBO/tugaspertemuan6/output_text_to_sound.mp3')  # Menyimpan suara ke file MP3
        playsound('E:/UMC/TUGAS SEMESTER GANJIL/PBO/tugaspertemuan6/output_text_to_sound.mp3')  # Memutar suara menggunakan playsound

# Membuat GUI
root = tk.Tk()
root.title("Text to Speech - Bahasa Indonesia")

# Widget Label
label = tk.Label(root, text="Masukkan Teks:")
label.pack(pady=10)

# Widget Entry
text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=10)

# Widget Button
convert_button = tk.Button(root, text="Konversi ke Suara", command=text_to_speech)
convert_button.pack(pady=20)

# Menjalankan loop GUI
root.mainloop()
