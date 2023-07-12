"""
En este archivo se presenta el código de una interfaz simple para el comparador de bloques TESA
"""

################## Importación de librerías ##################
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import  openpyxl

################## Definición variables globales ##################

cliente_combobox = None
certificado_entry = None
solicitud_entry = None
idCalibrando_entry = None
responsable_entry = None
revision_entry = None
patron_combobox = None
material_combobox = None
secuencia_combobox = None
tInicial_entry = None
tEstabilizacion_entry = None
numReps_entry = None
certificado_combobox = None

################## Definición de funciones para la interfaz ##################

def nueva_calibracion():
    #Destruir la ventana del menú de opciones una vez que se selecciona una opción
    for child in root.winfo_children():
        child.destroy()

    #Crear un nuevo layout para la ventana de Nueva Calibración
    title_label = ttk.Label(root, text="Comparador de bloques TESA", font=("Helvetica", 16, "bold"), background="white")
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    subtitle_label = ttk.Label(root, text="Nueva calibración", font=("Helvetica", 14), background="white")
    subtitle_label.grid(row=1, column=0, columnspan=2, pady=10)

    image = Image.open("logoLCM.png")  
    image = image.resize((int(image.width * 0.25), int(image.height * 0.25)))  #Ajustar el tamaño del logo
    image = ImageTk.PhotoImage(image)

    image_label = ttk.Label(root, image=image, background="white")
    image_label.image = image
    image_label.grid(row=0, column=2, rowspan=1, padx=10, pady=10)
    
    global cliente_combobox, certificado_entry, solicitud_entry, idCalibrando_entry, responsable_entry, revision_entry
    global revision_entry, patron_combobox, material_combobox, secuencia_combobox, tInicial_entry, tEstabilizacion_entry, numReps_entry
    
    #Crear una lista con los nombres de los clientes ya registrados
    clientesRegistrados = []
    archivoClientes = openpyxl.load_workbook("Clientes.xlsx")
    hojaClientes = archivoClientes.active
    
    numFila = 3 #Se empieza en la fila 3 porque antes están los encabezados
    for fila in hojaClientes.iter_rows(min_row=3,
                                        min_col=1,
                                        max_col=1):
        for celda in fila:
            if celda.value != None:
                clientesRegistrados.append(celda.value)
    archivoClientes.close()
    
    #Espacios para ingresar las variables requeridas para una nueva calibración
    cliente_label = ttk.Label(root, text="Nombre del cliente:", anchor=tk.CENTER, background="white")
    cliente_label.grid(row=2, column=0, pady=5, sticky=tk.EW)
    cliente_combobox = ttk.Combobox(root, values=clientesRegistrados, width=40)
    cliente_combobox.grid(row=2, column=1, columnspan=2, pady=5, padx=(20,5), sticky="ew")

    certificado_label = ttk.Label(root, text="Número de certificado:", background="white")
    certificado_label.grid(row=3, column=0, pady=5)
    certificado_entry = ttk.Entry(root, width=42)
    certificado_entry.grid(row=3, column=1, columnspan=2, pady=5, padx=(20,5))

    solicitud_label = ttk.Label(root, text="Número de solicitud:", background="white")
    solicitud_label.grid(row=4, column=0, pady=5)
    solicitud_entry = ttk.Entry(root, width=42)
    solicitud_entry.grid(row=4, column=1, columnspan=2, pady=5, padx=(20,5))
    
    idCalibrando_label = ttk.Label(root, text="Identificación del calibrando:", background="white")
    idCalibrando_label.grid(row=5, column=0, pady=5)
    idCalibrando_entry = ttk.Entry(root, width=42)
    idCalibrando_entry.grid(row=5, column=1, columnspan=2, pady=5, padx=(20,5))
    
    responsable_label = ttk.Label(root, text="Responsable de la calibración:", background="white")
    responsable_label.grid(row=6, column=0, pady=5)
    responsable_entry = ttk.Entry(root, width=42)
    responsable_entry.grid(row=6, column=1, columnspan=2, pady=5, padx=(20,5))
    
    revision_label = ttk.Label(root, text="Responsable de la revisión:", background="white")
    revision_label.grid(row=7, column=0, pady=5)
    revision_entry = ttk.Entry(root, width=42)
    revision_entry.grid(row=7, column=1, columnspan=2, pady=5, padx=(20,5))
    
    patron_label = ttk.Label(root, text="Patrón a utilizar:", anchor=tk.CENTER, background="white")
    patron_label.grid(row=8, column=0, pady=5, sticky=tk.EW)
    patron_combobox = ttk.Combobox(root, values=["Bloques Patrón de Cerámica de 0,05\" a 4\"","Bloques Patrón de Cerámica de 0,5 mm a 100 mm"], width=40)
    patron_combobox.grid(row=8, column=1, columnspan=2, pady=5, padx=(20,5), sticky="ew")
    
    material_label = ttk.Label(root, text="Material de los bloques patrón: ", anchor=tk.CENTER, background="white")
    material_label.grid(row=9, column=0, pady=5, sticky=tk.EW)
    material_combobox = ttk.Combobox(root, values=["Patrón en acero","Patrón en Tungsteno", "Patrón en cerámica", "Patrón en cromo"], width=40)
    material_combobox.grid(row=9, column=1, columnspan=2, pady=5, padx=(20,5), sticky="ew")
    
    secuencia_label = ttk.Label(root, text="Secuencia de calibración:", anchor=tk.CENTER, background="white")
    secuencia_label.grid(row=10, column=0, pady=5, sticky=tk.EW)
    secuencia_combobox = ttk.Combobox(root, values=["Desviación central","Desviación central y planitud"], width=40)
    secuencia_combobox.grid(row=10, column=1, columnspan=2, pady=5, padx=(20,5), sticky="ew")
    
    tInicial_label = ttk.Label(root, text="Tiempo inicial (en minutos):", background="white")
    tInicial_label.grid(row=11, column=0, pady=5)
    tInicial_entry = ttk.Entry(root, width=42)
    tInicial_entry.grid(row=11, column=1, columnspan=2, pady=5, padx=(20,5))
    
    tEstabilizacion_label = ttk.Label(root, text="Tiempo de estabilización (en segundos):", background="white")
    tEstabilizacion_label.grid(row=12, column=0, pady=5)
    tEstabilizacion_entry = ttk.Entry(root, width=42)
    tEstabilizacion_entry.grid(row=12, column=1, columnspan=2, pady=5, padx=(20,5))
    
    numReps_label = ttk.Label(root, text="Número de repeticiones:", background="white")
    numReps_label.grid(row=13, column=0, pady=5)
    numReps_entry = ttk.Entry(root, width=42)
    numReps_entry.grid(row=13, column=1, columnspan=2, pady=5, padx=(20,5))
    
    continuar_button = ttk.Button(root, text="Continuar", command=continuarNuevaCalibracion)
    continuar_button.grid(row=14, column=0, columnspan=1, pady=10)
    return

def reanudar_calibracion():
    #Destruir la ventana del menú de opciones una vez que se selecciona una opción
    for child in root.winfo_children():
        child.destroy()

    #Crear un nuevo layout para la ventana de Nueva Calibración
    title_label = ttk.Label(root, text="Comparador de bloques TESA", font=("Helvetica", 16, "bold"), background="white")
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    subtitle_label = ttk.Label(root, text="Reanudar calibración", font=("Helvetica", 14), background="white")
    subtitle_label.grid(row=1, column=0, columnspan=2, pady=10)

    image = Image.open("logoLCM.png")  
    image = image.resize((int(image.width * 0.25), int(image.height * 0.25)))  #Ajustar el tamaño del logo
    image = ImageTk.PhotoImage(image)

    image_label = ttk.Label(root, image=image, background="white")
    image_label.image = image
    image_label.grid(row=0, column=2, rowspan=1, padx=10, pady=10)
    
    global certificado_combobox, tInicial_entry, tEstabilizacion_entry
    
    #Se crea una lista con el nombre de los documentos que se encuentran en la carpeta de "Calibraciones en curso"
    calibracionesEnCurso = []
    for archivo in os.listdir("./Calibraciones en curso/"):
        if os.path.isfile(os.path.join("./Calibraciones en curso/",archivo)):
            nombreArchivo, extension = os.path.splitext(archivo)
            calibracionesEnCurso.append(nombreArchivo)
    
    #Espacios para ingresar las variables requeridas para reanudar calibración
    certificado_label = ttk.Label(root, text="Seleccione la calibración a reanudar:", anchor=tk.CENTER, background="white")
    certificado_label.grid(row=2, column=0, pady=5, sticky=tk.EW)
    certificado_combobox = ttk.Combobox(root, values=calibracionesEnCurso, width=40)
    certificado_combobox.grid(row=2, column=1, columnspan=2, pady=5, padx=(20,5), sticky="ew")
    
    tInicial_label = ttk.Label(root, text="Tiempo inicial (en minutos):", background="white")
    tInicial_label.grid(row=3, column=0, pady=5)
    tInicial_entry = ttk.Entry(root, width=42)
    tInicial_entry.grid(row=3, column=1, columnspan=2, pady=5, padx=(20,5))
    
    tEstabilizacion_label = ttk.Label(root, text="Tiempo de estabilización (en segundos):", background="white")
    tEstabilizacion_label.grid(row=4, column=0, pady=5)
    tEstabilizacion_entry = ttk.Entry(root, width=42)
    tEstabilizacion_entry.grid(row=4, column=1, columnspan=2, pady=5, padx=(20,5))
    
    reanudar_button = ttk.Button(root, text="Reanudar calibración", command=reanudarCalibracion)
    reanudar_button.grid(row=5, column=0, columnspan=1, pady=10)
    return

def ingresar_cliente():
    print("Ingresar cliente selected")
    return

def ingresar_calibrando():
    print("Ingresar calibrando selected")
    return

def continuarNuevaCalibracion():
    cliente = cliente_entry.get()
    certificado = certificado_entry.get()
    solicitud = solicitud_entry.get()
    idCalibrando = idCalibrando_entry.get()
    respondable = responsable_entry.get()
    revision = revision_entry.get()
    patron = patron_combobox.get()
    material = material_combobox.get()
    secuencia = secuencia_combobox.get()
    tInicial = tInicial_entry.get()
    tEstabilizacion = tEstabilizacion_entry.get()
    numReps = numReps_entry.get()  
    print("Yupi")  
    
def reanudarCalibracion():
    certificado = certificado_combobox.get()
    tInicial = tInicial_entry.get()
    tEstabilizacion = tEstabilizacion_entry.get()
    
################## Ventana inicial ##################

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
image_label.grid(row=0, column=2, rowspan=1, padx=10, pady=10)

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

