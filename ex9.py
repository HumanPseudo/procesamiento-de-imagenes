import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

cv2.imshow('example1', x)
cv2.imshow('example2', y)

k = cv2.waitKey(0)

print (cv2.add(x,y)) # 250+10 = 260 => 255
print (x+y) # 250+10 = 260 % 256 =4