
################## Importación de librerías ##################
import RPi.GPIO as GPIO                                             # Biblioteca para el control de los motores a pasos y el servomotor
from RpiMotorLib import RpiMotorLib                                 # Biblioteca para motores a pasos
from RpiMotorLib import rpiservolib                                 # Biblioteca para servomotor
from time import sleep                                              # Biblioteca para sleep
import time
import serial                                                       # Biblioteca para configuración y adquisición de datos de dispositivos seriales
import openpyxl                                                     # Biblioteca para hojas de datos
import smtplib, ssl
import pandas as pd                                                 # Biblioteca para manejo de datos
import numpy as np                                                  # Biblioteca para trabajar con arreglos, facilita operaciones matemáticas
import openpyxl                                                     # Biblioteca para el manejo de archivos de excel
from openpyxl import load_workbook                                  # Biblioteca para cargar excel ya existente
import openpyxl.utils.cell                                          # Biblioteca para insertar columnas o filas en un excel 
from openpyxl.styles import Font, Color, Alignment, Border, Side    # Biblioteca para darle formato a archivos de excel
import shutil                                                       # Biblioteca para copiar archivos
import datetime                                                     # Biblioteca para obtener información de la fecha y hora del día
from decimal import Decimal                                         # Biblioteca para trabajar correctamente operaciones aritméticas con flotantes decimales

################################################################

global motorEnabledState
global motorDisabledState 
motorEnabledState = GPIO.HIGH
motorDisabledState = GPIO.LOW

################## Configuración de entradas/salidas ##################

GPIO_pins1 = (22, 27, 17)           #pines de modo para el motor1
direction1 = 9                      #pin de dirección para el motor1
step1 = 11                          #pin de step para el motor1

GPIO_pins2 = (5, 6, 13)             #pines de modo para el motor2
direction2 = 20                     #pin de dirección para el motor2
step2 = 21                          #pin de step para el motor2

pin_enableCalibrationMotor = 24                         #pin de enable

GPIO_pins3 = (14, 15, 18)           #Pines de modo de paso
direction3 = 19                     #Pin de sentido de giro
step3 = 16                          #Pin de dar paso
pin_enablePlateMotor = 23

sleepMot3=12                        #Pin para controlar el sleep del motor de ordenamiento
                                    #Si está en 1 está activo, en 0 está en sleep
pin_startRotationLimitSensor = 4               #Pin para el sensor infrarrojo de rotacion de angulo nicial
pin_endRotationLimitSensor = 3                 #Pin para el sensor infrarrojo de rotacion de angulo final

steperMotorPlate = RpiMotorLib.A4988Nema(direction3, step3, GPIO_pins3, "A4988") #Parámetros del motor

steperMotor1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins1, "A4988") #Parámetros del motor1
steperMotor2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins2, "A4988") #Parámetros del motor2

GPIO.setup(pin_enableCalibrationMotor, GPIO.OUT)     
                                                                                                                                           
GPIO.output(pin_enableCalibrationMotor, motorDisabledState)       #Modo seguro, motores inhabilitados

GPIO.setup(pin_enablePlateMotor, GPIO.OUT)     
                                                                                                                                           
GPIO.output(pin_enablePlateMotor, motorDisabledState)       #Modo seguro, motores de plato inhabilitados

GPIO.setup(sleepMot3, GPIO.OUT)                                                                                                                                                
GPIO.output(sleepMot3, GPIO.LOW)       #Sleep debe estar en LOW para deshabilitarse


GPIO.setmode(GPIO.BCM)              #Numeración Broadcom
GPIO.setup(pin_startRotationLimitSensor, GPIO.IN)    #Se define como entrada el sensor

posicionStep=0                      #Variable de posición angular del disco
required=0                          #Variable de pasos requeridos par llegar
                                    #a la posicion deseada
listo=0                             #Variable que determina cuando terminó

#gohome()                            #gire el disco hasta home porque se inició el programa



def Centros(tiempoinicial, tiempoestabilizacion, Repeticiones):
    GPIO.output(pin_enableCalibrationMotor, motorEnabledState)       #habilita los motores
    
    global valorNominalBloque
    global dato
    
    #obtenerAnguloBloque(valorNominalBloque[dato])          #Moverse a la siguiente pareja de bloques
    global t1
    t1=time.time()                                   #finaliza el conteo de espera de bloques
    tic=time.perf_counter()                                 #Toma el tiempo inicial
    
    listaMediciones=[]
    
    #sleep(int(tiempoinicial)*60)
    
    for i in range(int(Repeticiones)):
        
                                                            #Se inicia en 1 y con palpador arriba

        #ActivaPedal(servo_pin)                              #Baja palpador
        #sleep(int(tiempoestabilizacion))                    #Tiempo de estabilización
        #ActivaPedal(servo_pin)                              #Sube palpador
        #MedicionBloque=DatosTESA()                   #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)              #Valor del patrón en posición 1 (centro)
     
        steperMotor1.motor_go(True, "Half", 407, .005, False, 2)
                                                            #Movimiento de punto1 a punto2
        
        #ActivaPedal(servo_pin)                              #Baja palpador
        #sleep(int(tiempoestabilizacion))                    #Tiempo de estabilización
        #ActivaPedal(servo_pin)                              #Sube palpador
        #MedicionBloque=DatosTESA()                   #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)               #Valor del calibrando en posición 2 (esquina)

        steperMotor1.motor_go(False, "Half", 410, .005, False, 2)

                                                            #Movimiento de punto2 a punto1
    
    #ActivaPedal(servo_pin)                                  #Baja palpador
    #sleep(int(tiempoestabilizacion))                        #Tiempo de estabilización
    #ActivaPedal(servo_pin)                                  #Sube palpador
    #MedicionBloque=DatosTESA()                       #Llama función TESA
    #print(MedicionBloque)
    #listaMediciones.append(MedicionBloque)                  #Valor del calibrando en posición 2 (esquina)

    steperMotor1.motor_go(True, "Half", 203, .005, False, 2)#Movimiento de punto1 a HOME

    #ActivaPedal(servo_pin)                                  #Baja palpador
    #obtenerAnguloBloque(valorNominalBloques[dato])          #Moverse a la siguiente pareja de bloques
    toc=time.perf_counter()                                 #Toma el tiempo final
    global tiempoCorrida
    tiempoCorrida=toc-tic                                   #retorna el tiempo de corrida en segundos
    global t0
    t0=time.time()                                   #inicia el conteo de espera de bloques
    GPIO.output(pin_enableCalibrationMotor, motorDisabledState)       #Inhabilita los motores
    #return listaMediciones, tiempoCorrida, t0
    return




Centros(1, 1, 1)
