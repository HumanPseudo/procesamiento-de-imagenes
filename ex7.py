import cv2
import numpy as np


img = cv2.imread('luci.png')
height, width, canales = img.shape
# print(height,'|',width,'|',canales)
a,b = round((height/2)),round((width/2))
# print(a,'|',b)
px = img[a,b]
# print (px)

# accessing only blue pixel
blue = img[a,b,0]
# print (blue)
img[a,b] = [255,255,255]


#------------------------------
# accessing RED value location method
#img.item(10,10,2)
# modifying RED value
# img.itemset((10,10,2),100)
# print(item)

# imprime alto, ancho (no estoy seguro del orden)y otro valor(buscar)
# print (img.shape)
# imprime el peso de la imagen
# print (img.size)
#imprime el formato sobre el que esta basado la imagen
# print (img.dtype)


#primera forma
# bl,g,r = cv2.split(img)

# 2da forma
# b = img[:,:,0]
# g = img[:,:,1]
# r = img[:,:,2]


#----------------------------
# Supongamos que quieres hacer que todos los píxeles rojos valgan cero, no necesitas dividirlos todos de esta forma y colocarlos igual a cero. Puedes simplemente usar indexación Numpy la cual es más rápida.

img[:,:,2] = 0
#----------------------------
#img = cv2.merge([b,g,r])



# print(img.shape)
cv2.imshow('image',img)
#cv2.imshow('bl',img)


# print(bl,g,r)
# out = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
# cv2.imshow('example', out)

k = cv2.waitKey(0)