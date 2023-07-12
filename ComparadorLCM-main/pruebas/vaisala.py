import serial
from time import sleep
serVaisala=serial.Serial('/dev/ttyUSBD', baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout= 0.5)

listaDatosPresVaisala=[]
listaDatosTempVaisala=[]
listaDatosHumeVaisala=[]


def DatosVaisala(serVaisala):
    serVaisala.write(b'FORM 4.2 " P=" P " " U6 3.2 "T=" T " " U3 3.2 "RH=" RH " " U4\r\n') # Formato para la toma de datos
    serVaisala.write(b'SEND\r\n')  #Envío de instrucción para capturar datos del Vaisala
    
    detenerse=0  #Constante para while que captura dato
    
    DatoPresVaisala=0
    DatoTempVaisala=0
    DatoHumeVaisala=0
    
    def recv(serial):
        while True:
            data=serial.read(85)
            #print(data)
            if data == '':
                continue
            else:
                break
            sleep(0.02)
        return data
        
        
    while detenerse == 0:
        data=recv(serVaisala)                   #Llamada de la función
        if data.split()[0] == b'OK': 						#Comparación de datos recibidos, vacío hasta que se de la medición
            todos=data.split()					#Separar los 4 datos en una lista
            print(data)
            
            DatoPresVaisala=float(todos[3]) #Guardando presión atmosférica en lista
            DatoTempVaisala=float(todos[6]) #Guardando temperatura en lista
            DatoHumeVaisala=float(todos[9]) #Guardando humedad relativa 3 en lista
            
            detenerse = 1
    return DatoPresVaisala, DatoTempVaisala, DatoHumeVaisala

print("Medición 1:")
DatoPresVaisala, DatoTempVaisala, DatoHumeVaisala=DatosVaisala(serVaisala)

listaDatosPresVaisala.append(DatoPresVaisala)
listaDatosTempVaisala.append(DatoTempVaisala)
listaDatosHumeVaisala.append(DatoHumeVaisala)

sleep(1)
print("Medición 2:")
DatoPresVaisala, DatoTempVaisala, DatoHumeVaisala=DatosVaisala(serVaisala)

listaDatosPresVaisala.append(DatoPresVaisala)
listaDatosTempVaisala.append(DatoTempVaisala)
listaDatosHumeVaisala.append(DatoHumeVaisala)


print(5*"-","\nResultados:\n")
print("Presión:",listaDatosPresVaisala)
print("Temperatura:",listaDatosTempVaisala)
print("Humedad:",listaDatosHumeVaisala)



    
