from picamera2 import Picamera2
import cv2
import numpy as np
from time import sleep
import datetime

real_height = 0.15 #meters
focal_length = 600 #need to calibrate
min_contour_area = 250 #need to calibrate
color_ranges = {
	"green": ([35, 50, 50], [90, 255, 255]),
	"red": ([0, 100, 100], [10, 255, 255]),
	"red2": ([160, 100, 100], [179, 255, 255]),
	"blue": ([100, 50, 50], [140, 255, 255])
}

def calc_dist(pixel_height, focal_length, real_height):
	distance = (real_height*focal_length)/pixel_height #meters
	return distance
def detect_objects(picam2):
	picam2.start()
	sleep(2)
	frame = picam2.capture_array()
	picam2.stop()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
	detected_objects = []
	
	for  color, (lower, upper) in color_ranges.items():
		mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
		if color == "red":
			mask2 = cv2.inRange(hsv, np.array(color_ranges["red2"][0]), np.array(color_ranges["red2"][1]))
			mask = cv2.bitwise_or(mask, mask2)
		contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		if contours:
			filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
			if filtered_contours:
				largest_contour = max(filtered_contours, key=cv2.contourArea)
				x, y, w, h = cv2.boundingRect(largest_contour)
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
				distance = calc_dist(h, focal_length, real_height)
				center_x = x+w//2
				center_y = y+h//2
				cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)
				  
				detected_objects.append({
					"color": color,
					"center_x": center_x,
					"center_y": center_y,
					"distance": distance
				})
			
	cv2.imshow("Image", frame)
	#cv2.waitKey(1)
	return detected_objects
def write_to_file(data, filename="cont.txt"):
	with open(filename, "w") as file:
		if data:
			for obj in data:
				file.write(f"{obj['color']} ({obj['center_x']},{obj['center_y']}) {obj['distance']:.2f} \n") 
		else:
			file.write("None")

picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)

while 1:
	det_data = []
	detected_data = detect_objects(picam2)
	print(detected_data)
	m=100000000
	for h in detected_data:
		n = h["distance"]
		m = min(n,m)
	for j in detected_data:
		if j["distance"] == m:
			det_data.append(j)
			break
		
	print(det_data)
	write_to_file(det_data)
	
	
	if cv2.waitKey(1) == 27: 
		break
cv2.destroyAllWindows()

					
