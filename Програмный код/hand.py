import RPi.GPIO as GPIO
from time import sleep
import cv2

s_1step = 27
s_2step = 22
s_claw = 25  
s_turn = 17

contact = open("/home/d42/Desktop/1/cont.txt", 'r')                                     

GPIO.setmode(GPIO.BCM)
GPIO.setup(s_1step, GPIO.OUT)
GPIO.setup(s_2step, GPIO.OUT)
GPIO.setup(s_claw, GPIO.OUT)
GPIO.setup(s_turn, GPIO.OUT)

def set_angle(servo, angle):
	s = GPIO.PWM(servo, 50)
	s.start(8)
	duty = angle/18. + 2
	s.ChangeDutyCycle(duty)
	sleep(0.3)
	s.stop()
set_angle(s_1step, 0)	
set_angle(s_2step, 0)	
set_angle(s_claw, 0)	
set_angle(s_turn, 0)	
while 1:
	contact.seek(0)
	text=list(map(str, contact.read().split()))
	try:
		text[2]=float(text[2])
	except IndexError:
		print("None") 
	if not (text[0] == "None"):                                                                                                                    
		if text[0] == "blue":
			
		elif rext[0] == "green":
			

			
			
