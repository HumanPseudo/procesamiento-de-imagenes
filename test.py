import numpy as np


height = 100
width = 100
img1 = np.zeros((height,width,3),np.uint8)
img2 = np.zeros(10)

row,cols,channels = img1.shape
roi = img1[0:row, 0:cols]

#img1gris = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)


# print(roi)
print('img1.shape: '+str(img1.shape))
print('roi.shape: '+str(roi.shape))
#print('img1gris.shape: '+str(img1gris.shape))

# cv2.imshow('img1',img1)
# cv2.imshow('roi',roi)
# cv2.imshow('img1gris',img1gris)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if roi.all==img1.all:
    print('ok')
else:
    print('not ok')

