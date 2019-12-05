import numpy as np
import cv2
cap = cv2.VideoCapture(1)

while(True):
  # Captura video cuadro a cuadro 
  ret, frame = cap.read()
  # Nuestras operaciones sobre los cuadros se hacen aqui
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Muestra el cuadro resultante
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# Cuando todo está listo, se libera la captura 
cap.release()
cv2.destroyAllWindows()