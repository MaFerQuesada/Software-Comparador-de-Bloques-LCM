import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def nueva_calibracion():
    # Destroy the previous window
    for child in root.winfo_children():
        child.destroy()

    # Create the new layout
    title_label = ttk.Label(root, text="Comparador de bloques TESA", font=("Helvetica", 16, "bold"), background="white")
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    subtitle_label = ttk.Label(root, text="Nueva Calibración", font=("Helvetica", 14), background="white")
    subtitle_label.grid(row=1, column=0, columnspan=2, pady=10)

    image = Image.open("logoLCM.png")  # Replace "logoLCM.png" with your image file
    image = image.resize((int(image.width * 0.25), int(image.height * 0.25)))  # Resize the image
    image = ImageTk.PhotoImage(image)

    image_label = ttk.Label(root, image=image, background="white")
    image_label.image = image
    image_label.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

    entry1_label = ttk.Label(root, text="Entry 1:", background="white")
    entry1_label.grid(row=2, column=0, pady=5)
    entry1_entry = ttk.Entry(root)
    entry1_entry.grid(row=2, column=1, pady=5)

    entry2_label = ttk.Label(root, text="Entry 2:", background="white")
    entry2_label.grid(row=3, column=0, pady=5)
    entry2_entry = ttk.Entry(root)
    entry2_entry.grid(row=3, column=1, pady=5)

    entry3_label = ttk.Label(root, text="Entry 3:", background="white")
    entry3_label.grid(row=4, column=0, pady=5)
    entry3_entry = ttk.Entry(root)
    entry3_entry.grid(row=4, column=1, pady=5)

    continuar_button = ttk.Button(root, text="Continuar", command=continuar)
    continuar_button.grid(row=5, column=0, columnspan=2, pady=10)

def reanudar_calibracion():
    print("Reanudar calibración selected")

def ingresar_cliente():
    print("Ingresar cliente selected")

def ingresar_calibrando():
    print("Ingresar calibrando selected")

def continuar():
    value1 = entry1_entry.get()
    value2 = entry2_entry.get()
    value3 = entry3_entry.get()
    print("Entry 1:", value1)
    print("Entry 2:", value2)
    print("Entry 3:", value3)

root = tk.Tk()
root.title("Comparador de bloques TESA")
root.configure(bg="white")

title_label = ttk.Label(root, text="Comparador de bloques TESA", font=("Helvetica", 16, "bold"), background="white")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

subtitle_label = ttk.Label(root, text="Menú de opciones", font=("Helvetica", 14), background="white")
subtitle_label.grid(row=1, column=0, columnspan=2, pady=10)

image = Image.open("logoLCM.png")  # Replace "logoLCM.png" with your image file
image = image.resize((int(image.width * 0.25), int(image.height * 0.25)))  # Resize the image
image = ImageTk.PhotoImage(image)

image_label = ttk.Label(root, image=image, background="white")
image_label.image = image
image_label.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

options = [
    ("Nueva calibración", nueva_calibracion),
    ("Reanudar calibración", reanudar_calibracion),
    ("Ingresar cliente", ingresar_cliente),
    ("Ingresar calibrando", ingresar_calibrando)
]

for i, (text, command) in enumerate(options):
    button = ttk.Button(root, text=text, command=command)
    button.grid(row=i+2, column=0, columnspan=2, pady=5, padx=10, sticky="we")

root.mainloop()

