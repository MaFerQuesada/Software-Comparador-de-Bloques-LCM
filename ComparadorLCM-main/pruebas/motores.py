import RPi.GPIO as GPIO                                             # Biblioteca para el control de los motores a pasos y el servomotor
from RpiMotorLib import RpiMotorLib                                 # Biblioteca para motores a pasos
from RpiMotorLib import rpiservolib                                 # Biblioteca para servomotor
from time import sleep                                              # Biblioteca para sleep
import time
import serial                                                       # Biblioteca para configuración y adquisición de datos de dispositivos seriales




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
GPIO.setup(pin_startRotationLimitSensor, GPIO.IN)
GPIO.setup(pin_endRotationLimitSensor, GPIO.IN)    #Se define como entrada el sensor

posicionStep=0                      #Variable de posición angular del disco
required=0                          #Variable de pasos requeridos par llegar
                                    #a la posicion deseada
listo=0                             #Variable que determina cuando terminó

#gohome()                            #gire el disco hasta home porque se inició el programa



#funcion de prueba del movimiento para los motores
"""
def Prueba():
	
	# Motores TESA
	#GPIO.output(pin_enableCalibrationMotor, motorEnabledState)   
	#steperMotor1.motor_go(True, "Half", 200, 0.05, True, 2)
	
	#steperMotor1.motor_go(False, "Half", 96, .005, False, 2) #Mov1 de 2 a 3
	#steperMotor2.motor_go(False, "Full", 398, .005, True, 1) #Mov2 de 2 a 3
    #steperMotor1.motor_go(True, "Half", 178, .005, False, 1) #Mov3 de 2 a 3
	
	#GPIO.output(pin_enableCalibrationMotor, motorDisabledState)   
	return
"""

def PlatoGoHome():
	"""
	Lleva el Plato Giratorio a la posición inicial Home. Suponiendo un movimiento siempre a favor de las agujas del reloj,
	se pone a girar al sentido contrario hasta llegar a la posición inicial
	"""
	# Preparación del Motor
	GPIO.output(pin_enablePlateMotor, motorEnabledState)
	GPIO.output(sleepMot3, GPIO.HIGH) 
	
	run = True
	while run:
		
		steperMotorPlate.motor_go(False, "1/4", 20, 0.005, False, 0) # Hacer un movimiento de aprox 2 grados
		
		if GPIO.input(pin_startRotationLimitSensor) or GPIO.input(pin_endRotationLimitSensor): 
			# Si alguno de los sensores se activa, detener
			run = False
	
		# Vuelta del motor al LOW
	GPIO.output(sleepMot3, GPIO.LOW) 
	GPIO.output(pin_enablePlateMotor, motorDisabledState)
	
	
	return
	
	
	
def PlatoGo(sector):
	"""
	Lleva el Plato Giratorio a la posición inicial Home para luego transportarlo al sector indicado en la entrada.
	
	INPUT: sector (int): Sector del 1 al 4 que se desea colocar en el plato.
	"""
	
	PlatoGoHome()
	
	if isinstance(sector, int) and 1<= sector <=4:
			# Preparación del Motor
		GPIO.output(pin_enablePlateMotor, motorEnabledState)
		GPIO.output(sleepMot3, GPIO.HIGH)  
			# Giro al sector
		steperMotorPlate.motor_go(True, "1/4", 824*sector, 0.005, False, 0) # Intento de vuelta completa con step de 1/4
			# Vuelta del motor al LOW
		GPIO.output(sleepMot3, GPIO.LOW)
		GPIO.output(pin_enableCalibrationMotor, motorDisabledState)
	else:
		print("Fallo: Revise que el sector sea entero y un valor entre 1 y 4")
	
	return



def TesaGoOne():
	GPIO.output(pin_enableCalibrationMotor, motorEnabledState)
	GPIO.output(sleepMot3, GPIO.HIGH) 

	#steperMotor1.motor_go(True, "1/8", 413, .0025, False, 2)
	#steperMotor1.motor_go(False, "1/8", 413, .0025, False, 2)
	steperMotor2.motor_go(False, "Full", 337, .005, True, 1)   #1 a 4
	steperMotor2.motor_go(True, "Full", 337, .005, True, 1)   #4 a centro
	
	GPIO.output(sleepMot3, GPIO.LOW)
	GPIO.output(pin_enableCalibrationMotor, motorDisabledState)
	return

TesaGoOne()

GPIO.cleanup()
