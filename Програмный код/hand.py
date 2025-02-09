import RPi.GPIO as GPIO
from time import sleep
import cv2

s_1step = 27
s_2step = 22
s_3step = 19
s_claw = 25  
s_turn = 17

contact = open("/home/d42/Desktop/1/cont2.txt", 'r')                                     

GPIO.setmode(GPIO.BCM)
GPIO.setup(s_1step, GPIO.OUT)
GPIO.setup(s_2step, GPIO.OUT)
GPIO.setup(s_3step, GPIO.OUT)
GPIO.setup(s_claw, GPIO.OUT)
GPIO.setup(s_turn, GPIO.OUT)

def set_angle(servo, angle):
	s = GPIO.PWM(servo, 50)
	s.start(8)
	duty = angle/18. + 2
	s.ChangeDutyCycle(duty)
	sleep(0.3)
	s.stop()
def start_position():
	set_angle(s_turn, 0)
	set_angle(s_1step, 0)
	set_angle(s_claw, 0)		
	set_angle(s_3step, 0)
	set_angle(s_2step, 0)	
	
	
start_position()	
while 1:
	contact.seek(0)
	text=str(contact.read())
	if not text == "None":                                                                                                                    
		if text[0] == "blue":
			set_angle(s_3step, 90)
			set_angle(s_2step, 90)
			set_angle(s_1step, 90)
			set_angle(s_claw, 90)
			sleep(1)
			set_angle(s_claw, 0)
			set_angle(s_1step, 0)
			sleep(10)
			set_angle(s_1step, 90)
			set_angle(s_claw, 90)
			sleep(1)
			start_position()
		elif rext[0] == "green":
			set_angle(s_3step, 90)
			set_angle(s_2step, 90)
			set_angle(s_1step, 90)
			set_angle(s_claw, 90)
			sleep(1)
			set_angle(s_claw, 0)
			set_angle(s_1step, 0)
			set_angle(s_turn, 90)
			sleep(1)
			set_angle(s_3step, 0)
			set_angle(s_claw, 90)
			sleep(1)
			start_position()
		elif text == "yellow":
			set_angle(s_3step, 90)
			set_angle(s_claw, 90)
			set_angle(s_turn, 90)
			sleep(3)
			set_angle(s_claw, 0)
			set_angle(s_2step, 90)
			set_angle(s_turn, 0)
			sleep(1)
			set_angle(s_1step, 90)
			set_angle(s_claw, 90)
			sleep(2)
			start_position()
			
			
			

			
			
