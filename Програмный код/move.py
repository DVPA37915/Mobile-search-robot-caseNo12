import RPi.GPIO as GPIO
from time import sleep
import cv2

GPIO.setmode(GPIO.BCM)
contact = open("/home/d42/Desktop/1/cont.txt", 'r')

Lsens = 21
Csens = 16
Rsens = 20
GPIO.setup(Lsens, GPIO.IN)
GPIO.setup(Csens, GPIO.IN)
GPIO.setup(Rsens, GPIO.IN)

LpwmP = 13
LcwP = 23
LacwP = 24
RpwmP = 12
RcwP = 5
RacwP = 6
GPIO.setup(LpwmP, GPIO.OUT)
GPIO.setup(LcwP, GPIO.OUT)
GPIO.setup(LacwP, GPIO.OUT)
GPIO.setup(RpwmP, GPIO.OUT)
GPIO.setup(RcwP, GPIO.OUT)
GPIO.setup(RacwP, GPIO.OUT)

class motor:
	LpwmP = 13
	LcwP = 23
	LacwP = 24
	RpwmP = 12
	RcwP = 5
	RacwP = 6
	def move(speed, time):
		Speed = GPIO.PWM(LpwmP, 50)
		Speed2 = GPIO.PWM(RpwmP, 50)
		Speed.start(speed)
		Speed2.start(speed)
		GPIO.output(LcwP, 1)
		GPIO.output(LacwP, 0)
		GPIO.output(RcwP, 1)
		GPIO.output(RacwP, 0)
		sleep(time)
		Speed.stop()
		Speed2.stop()
	def r_turn(speed, angle):
		Speed = GPIO.PWM(LpwmP, 50)
		Speed2 = GPIO.PWM(RpwmP, 50)
		Speed.start(speed)
		Speed2.start(speed)
		GPIO.output(LcwP, 0)
		GPIO.output(LacwP, 1)
		GPIO.output(RcwP, 1)
		GPIO.output(RacwP, 0)
		sleep(angle/18.) #need to calibrate                                                                           
		Speed.stop()
		Speed2.stop()
	def l_turn(speed, angle):
		Speed = GPIO.PWM(LpwmP, 50)
		Speed2 = GPIO.PWM(RpwmP, 50)
		Speed.start(speed)
		Speed2.start(speed)
		GPIO.output(LcwP, 1)
		GPIO.output(LacwP, 0)
		GPIO.output(RcwP, 0)
		GPIO.output(RacwP, 1)
		sleep(angle/18.) #need to calibrate
		Speed.stop()
		Speed2.stop()

while 1:
	contact.seek(0)
	text=list(map(str, contact.read().split()))
	try:
		text[2]=float(text[2])
	except IndexError:
		print("None")
	
	if text[0] == "None" or text[2] >= 0.15:
		if not GPIO.input(Csens) == 1:
			if not GPIO.input(Lsens) == 1:
				if not GPIO.input(Rsens) == 1:
					motor.l_turn(50, 90)
				else:
					motor.move(50, 1)
			elif not GPIO.input(Rsens) == 1:
				motor.r_turn(50, 90)
			else:
				motor.move(50, 1)
		else:
			if not GPIO.input(Lsens) == 1:
				if not GPIO.input(Rsens) == 1:
					motor.r_turn(50, 90)
				else:
					motor.l_turn(50, 90)
			elif not GPIO.input(Rsens) == 1:
				motor.r_turn(50, 90)
			else:
				motor.l_turn(50, 180)
	else:
		if text[0] == "blue":  #need to calibrate
			motor.move(50, 3)
			sleep(20)
		elif text[0] == "green":
			motor.move(50, 3)
			sleep(15)
			motor.l_turn(50, 180)
		else:
			motor.l_turn(50, 90)
			motor.move(50, 6)
			motor.r_turn(50, 90)
			motor.move(50, 12)
			motor.r_turn(50, 90)
			motor.move(50, 6)
			motor.l_turn(50, 90)
				

			
	
	if cv2.waitKey(1) == 27:
		break
