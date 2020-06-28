import cv2
import numpy as np
import time


cap = cv2.VideoCapture(0)
time.sleep(1)
background = 0
for i in range(30):
    ret, background = cap.read()

background = np.flip(background, axis=1)

while (cap.isOpened()):
    ret, img = cap.read()
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)
    blurred = cv2.GaussianBlur(hsv, value, 0)

    lower_red = np.array([0,108,73])
    upper_red = np.array([9,255,255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    img[np.where(mask1 == 255)] = background[np.where(mask1 == 255)]
    cv2.imshow('Display', img)

    key = cv2.waitKey(1)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break