#pip install opencv-python
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Importa e converta para RGB
img = cv2.imread('./images/Satelite.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Convertendo para preto e branco (RGB -> Gray Scale -> BW)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
a = img_gray.max()
_, thresh = cv2.threshold(img_gray, a/2*1.7, a,cv2.THRESH_BINARY_INV)

tamanhoKernel = 40
kernel = np.ones((tamanhoKernel,tamanhoKernel), np.uint8)
img_grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)

# contorno usando a imagem img_grad (melhor imagem gerada pelo operadorMorfologico)
contours, hierarchy = cv2.findContours(
                                   image = img_grad,
                                   mode = cv2.RETR_TREE,
                                   method = cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)
img_copy = img.copy()
final = cv2.drawContours(img_copy, contours, contourIdx = -1,
                         color = (255, 0, 0), thickness = 2)

#plot imagens
imagens = [img,img_gray,thresh,img_grad,final]
formatoX = math.ceil(len(imagens)**.5)

if (formatoX**2-len(imagens))>formatoX:
    formatoY = formatoX-1
else:
    formatoY = formatoX

for i in range(len(imagens)):
    plt.subplot(formatoY, formatoX, i + 1)
    plt.imshow(imagens[i],'gray')
    plt.xticks([]),plt.yticks([])    
cv2.imshow("Imagem Gradiente", img_grad)
cv2.imshow("Imagem Final", final)

cv2.imwrite("Gradiente_Satelite.png", img_grad)
cv2.imwrite("Final_Satelite.png", final)
plt.show()