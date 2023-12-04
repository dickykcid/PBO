import tkinter as tk
from PIL import Image, ImageTk
import pytesseract

class ImageToTextConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image to Text Converter")

        # Tambahkan path Tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Tampilkan teks instruksi
        instruction_label = tk.Label(master, text="Gambar akan dikonversi ke teks:")
        instruction_label.pack()

        # Buka gambar
        image_path = "E:/UMC/TUGAS SEMESTER GANJIL/PBO/tugaspertemuan6/sampletext2.png"  # Ganti dengan path gambar Anda
        self.image = Image.open(image_path)

        # Tampilkan gambar di canvas
        self.canvas = tk.Canvas(master, width=450, height=100)
        self.canvas.pack()
        self.display_image()

        # Konversi gambar ke teks
        convert_button = tk.Button(master, text="Konversi ke Teks", command=self.convert_image_to_text)
        convert_button.pack()

        # Area teks untuk menampilkan hasil konversi
        self.text_display = tk.Text(master, height=5, width=60)
        self.text_display.pack()

    def display_image(self):
        # Menampilkan gambar di canvas
        photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def convert_image_to_text(self):
        # Melakukan konversi gambar ke teks
        text = pytesseract.image_to_string(self.image)
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextConverterApp(root)
    root.mainloop()
