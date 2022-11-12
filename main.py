import cv2

cap = cv2.VideoCapture(0)

def nothing(self):
	pass
	
cv2.namedWindow("filter")

cv2.createTrackbar("Hue","filter",0,255,nothing)
cv2.createTrackbar("Saturation","filter", 0, 255, nothing)
cv2.createTrackbar("Value", "filter", 0, 255, nothing)

while True:
	rep, frame = cap.read()
	hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	h_l = cv2.getTrackbarPos("Hue", "filter")
	s_l = cv2.getTrackbarPos("Saturation", "filter")
	v_l = cv2.getTrackbarPos("Value", "filter")

	lower = (h_l, s_l, v_l)
	higher = (255, 255, 255)

	mask = cv2.inRange(hsv, lower, higher)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow("result", res)
	cv2.imshow("mask", mask)

	if cv2.waitKey(1) == ord('q'):
		break