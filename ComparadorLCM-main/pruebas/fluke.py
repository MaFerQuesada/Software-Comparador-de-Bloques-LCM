import serial
from time import sleep
serFluke=serial.Serial("/dev/ttyUSBK", baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE, xonxoff=True, timeout=0.5) #Configuración de puerto


def DatosFluke():
    
    serFluke.write(b"READ?1\r\n") #Envío de instrucción para capturar dato de temperatura 1
    serFluke.write(b"READ?2\r\n") #Envío de instrucción para capturar dato de temperatura 2
    serFluke.write(b"READ?3\r\n") #Envío de instrucción para capturar dato de temperatura 3
    serFluke.write(b"READ?4\r\n") #Envío de instrucción para capturar dato de temperatura 4

    detenerse=0 #Constante para while que captura dato
    
    MedicionTemp1=0 #Creación de variable para almacenar mediciones de temperatura 1
    MedicionTemp2=0 #Creación de variable para almacenar mediciones de temperatura 2
    MedicionTemp3=0 #Creación de variable para almacenar mediciones de temperatura 3
    MedicionTemp4=0 #Creación de variable para almacenar mediciones de temperatura 4


    def recv(serial): #Definición de una función para recibir datos
        while True:
            data=serial.read(32) #Lectura de 32 bytes
            if data == "":
                continue
            else:
                break
            sleep(0.02)
        return data
    while detenerse == 0:
        data=recv(serFluke) #Llamada de la función
        print(data)
        if data != b"": #Comparación de datos recibidos, vacío hasta que se de la medición
            todas=data.split()#Separar los 4 datos en una lista
            MedicionTemp1=float(todas[0]) #Guardando temperatura 1 en lista
            MedicionTemp2=float(todas[1]) #Guardando temperatura 2 en lista
            MedicionTemp3=float(todas[2]) #Guardando temperatura 3 en lista
            MedicionTemp4=float(todas[3]) #Guardando temperatura 4 en lista
            detenerse = 1  #Condición para salir del while
    return MedicionTemp1, MedicionTemp2, MedicionTemp3, MedicionTemp4

print(DatosFluke())
