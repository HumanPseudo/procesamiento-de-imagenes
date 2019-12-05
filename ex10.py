import cv2

img1 = cv2.imread('joji.jpg')
img2 = cv2.imread('luci.png')
img3= img1[1:353,1:201,:]

print(img3.shape)
print(img2.shape)
print(img1.shape)

dst = cv2.addWeighted(img3,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
#cv2.imwrite('dst.png',dst)
cv2.waitKey(0)

cv2.destroyAllWindows()