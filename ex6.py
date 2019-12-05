import numpy as np
import cv2

# Crea una imagen en negro
img = np.zeros((512,512,3), np.uint8)

# Dibuja una línea horizontal verde con un grosor de 2px
img = cv2.line(img,(0,255),(511,255),(0,255,0),2)

# Dibuja un rectangulo azul con un grosor de 3px
img = cv2.rectangle(img,(210,360),(300,500),(255,0,0),3)

# Dibuja un circulo rojo con -1 es relleno
img = cv2.circle(img,(255,255), 100, (0,0,255), 1)

# Dibuja una media elipse
img = cv2.ellipse(img,(255,105),(100,50),0,0,180,255,1)

# Dibuja una elipse completa
img = cv2.ellipse(img,(255,200),(100,50),0,0,360,255,1)

# Dibuja poligono (triangulo)
pts = np.array([[180,120],[330,120],[255,140]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Tittle',(40,90), font, 4,(255,4,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
k = cv2.waitKey(0)

