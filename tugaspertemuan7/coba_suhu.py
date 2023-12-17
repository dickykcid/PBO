import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry_input.get())
        selected_input_unit = get_selected_input_unit()
        selected_output_unit = combo_output_unit.get()

        if selected_input_unit == selected_output_unit:
            result_var.set(f"{value} {selected_input_unit} = {value} {selected_output_unit}")
        else:
            result = kalkulasi_konversi(value, selected_input_unit, selected_output_unit)
            result_var.set(f"{value} {selected_input_unit} = {result:.2f} {selected_output_unit}")

    except ValueError as e:
        result_var.set("Error: " + str(e))

def kalkulasi_konversi(nilai, input_unit, output_unit):
    if input_unit == output_unit:
        return nilai
    elif input_unit == "Celsius" and output_unit == "Fahrenheit":
        return (nilai * 9/5) + 32
    elif input_unit == "Fahrenheit" and output_unit == "Celsius":
        return (nilai - 32) * 5/9
    elif input_unit == "Celsius" and output_unit == "Kelvin":
        return nilai + 273.15
    elif input_unit == "Kelvin" and output_unit == "Celsius":
        return nilai - 273.15
    elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
        celsius = (nilai - 32) * 5/9
        return celsius + 273.15
    elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
        celsius = nilai - 273.15
        return (celsius * 9/5) + 32
    else:
        raise ValueError("Pilihan tidak valid.")

def get_selected_input_unit():
    if checkbox_celsius.get():
        return "Celsius"
    elif checkbox_fahrenheit.get():
        return "Fahrenheit"
    elif checkbox_kelvin.get():
        return "Kelvin"
    else:
        raise ValueError("Pilih satu satuan suhu awal.")

app = tk.Tk()
app.title("Konverter Suhu")

frame = tk.Frame(app)
frame.pack(padx=40, pady=40)

label_input = tk.Label(frame, text="Masukkan suhu:")
label_input.grid(row=1, column=0, padx=5, pady=5)

entry_input = tk.Entry(frame)
entry_input.grid(row=2, column=0, padx=5, pady=5)

label_output_unit = tk.Label(frame, text="Konversi ke satuan:")
label_output_unit.grid(row=3, column=0, padx=5, pady=5)

combo_output_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_output_unit.grid(row=4, column=0, padx=5, pady=5)
combo_output_unit.set("Celsius")

checkbox_celsius = tk.Checkbutton(frame, text="Celsius")
checkbox_celsius.grid(row=5, column=0, padx=5, pady=5)

checkbox_fahrenheit = tk.Checkbutton(frame, text="Fahrenheit")
checkbox_fahrenheit.grid(row=6, column=0, padx=5, pady=5)

checkbox_kelvin = tk.Checkbutton(frame, text="Kelvin")
checkbox_kelvin.grid(row=7, column=0, padx=5, pady=5)

button_convert = tk.Button(frame, text="Konversi", command=convert)
button_convert.grid(row=8, column=0, padx=5, pady=5)

result_var = tk.StringVar()
label_result = tk.Label(frame, textvariable=result_var)
label_result.grid(row=9, column=0, padx=5, pady=5)

app.mainloop()
