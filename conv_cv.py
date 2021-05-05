import numpy as np
import cv2
#Se carga la imagen
img = cv2.imread('Turquia.jpg')

#Filtro para Simple Box Blur
sbb_kernel = np.array([[1/9, 1/9, 1/9], 
                       [1/9, 1/9, 1/9], 
                       [1/9, 1/9, 1/9]])

#Filtro para Edge Detection 
ed_kernel = np.array([[-1, -1, -1], 
                      [-1, 8,  -1], 
                      [-1, -1, -1]])

#Se filtra la imagen usando el kernel para Simple Box Blur
sbb_img = cv2.filter2D(img, -1, sbb_kernel)

#Se filtra la imagen usando el kernel para Edge Detection
ed_img = cv2.filter2D(img, -1, ed_kernel)

#Se exportan las imagenes resultantes de los filtros
cv2.imwrite('Turquia_SBB.jpg', sbb_img)
cv2.imwrite('Turquia_ED.jpg', ed_img)