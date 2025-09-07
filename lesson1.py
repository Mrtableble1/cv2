import cv2

image = cv2.imread(r"opencv/pika.png",0)
#cv2.IMREAD_COLOR(1)

#cv2.IMREAD_GRAYSCALE(0)

#cv2.IMREAD_UNCHANGED(-1)

cv2.imshow("pikachu",image)

cv2.waitKey(0)


image = cv2.imread(r"opencv/pika.png",0)
cv2.imshow("pikachu in black and white",image)
cv2.imwrite("greypika.png",image)
print("saved")

#splitting a image into RGB channels

image = cv2.imread(r"opencv/pika.png",1)
B,G,R=cv2.split(image)
cv2.imshow("pikachu in Blue",B)


cv2.imshow("pikachu in green",G)


cv2.imshow("pikachu in Red",R)

cv2.waitKey(0)