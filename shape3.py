import cv2
import numpy as np

#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 3)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (147, 96, 44), 3)

img = cv2.rectangle(img, (155, 155), (510,390), (0, 0, 255), 3)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), 4)
font = cv2.FONT_ITALIC
img = cv2.putText(img, 'openCv', (10, 500), font, 4, (255,255,255), 10, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()