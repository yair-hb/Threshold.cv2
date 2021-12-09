import cv2
import numpy as np
import imutils

imagen = cv2.imread('img.jpg',0)
imagen = imutils.resize(imagen, width =400)

#binary
_, binarizada = cv2.threshold(imagen, 210,255,cv2.THRESH_BINARY)
#binary inv
_, binarizada_inv = cv2.threshold(imagen, 210, 255,cv2.THRESH_BINARY_INV)
#truncate
_, trunc = cv2.threshold(imagen, 210, 255, cv2.THRESH_TRUNC)
#tozero 
_, tozero = cv2.threshold(imagen, 210, 255, cv2.THRESH_TOZERO)
#Tozero inv
_, tozero_inv =cv2.threshold(imagen, 210,255, cv2.THRESH_TOZERO_INV)

cv2.imshow('IMAGEN DE PRUEBA', imagen)
cv2.imshow('TIPOS: Binary - Binary-inv - Truncate', np.hstack([binarizada, binarizada_inv, trunc]))
cv2.imshow('TIPOS: TO ZERO - TO ZERO-INV', np.hstack([tozero, tozero_inv]))
cv2.waitKey(0)
cv2.destroyAllWindows()