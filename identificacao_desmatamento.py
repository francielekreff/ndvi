# -*- coding: utf-8 -*-
"""
Identificação de Áreas de Desmatamento Utilizando NDVI

Processamento Digital de Sinais 2023/1

Franciele Kreff e Tábata Ariel Pohren
"""

# Importação de bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Pré-processamento
# Função de rotação
def rotation(img):
    
    rows,cols = img.shape

    # cols-1 e rows-1 são os limites das coordenadas. 
    # Os dois primeiros parametros são o centro da imagem, ou o centro de rotação.
    # O terceiro parâmetro é o angulo de rotação. O ultimo parametro é o fator de escala.    
   
    M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),8.53,1)
    # Satélite Cbers 4 -> Azimuth 8.537181. 
    
    im_dst = cv2.warpAffine(img,M,(cols,rows))

    return  im_dst

# Função de recorte
def crop(img):
    
    # Monta o retangulo para ser o alvo do corte.
    y=5200
    x=1500
    h=175
    w=185

    crop_img = img[y:y+h, x:x+w]
    
    return crop_img

# Processamento
# Função de cálculo do NDVI
def calcula_ndvi(image_red, image_nir):
    bottom = (image_nir.astype(float) + image_red.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (image_nir.astype(float) - image_red.astype(float)) / bottom
    return ndvi

# Carrega a imagem vermelha (RED) - Banda 7
image_red = cv2.imread('CBERS_4_MUX_20230520_178_104_L4_BAND7.tif', -1)

# Carrega a imagem infravermelha (NIR) - Banda 8
image_nir = cv2.imread('CBERS_4_MUX_20230520_178_104_L4_BAND8.tif', -1)

#plt.imshow(image_nir, cmap=None) # Imagem original NIR

# Rotaciona imagens
image_red = rotation(image_red)
image_nir = rotation(image_nir)

# Corta imagens
image_red = crop(image_red)
image_nir = crop(image_nir)

# Converte a imagem para um array
image_red = np.array(image_red, dtype=float)/float(255)
image_nir = np.array(image_nir, dtype=float)/float(255)

# Calcula NDVI
image_ndvi = calcula_ndvi(image_red, image_nir)

# Cria nova imagem preta
new_image = np.zeros((image_ndvi.shape[0], image_ndvi.shape[1], 3), dtype=np.uint8)

# Monta mapa de NDVI
for i in range(len(image_ndvi)):
    for j in range(len(image_ndvi[0])):
        
        # Rios 
        if image_ndvi[i][j] <= 0.35:
            new_image[i, j, 2] = 255
                             
        # Vegetação
        elif image_ndvi[i][j] > 0.35 and image_ndvi[i][j] <= 0.40:
            new_image[i, j, 1] = 150
        
        elif image_ndvi[i][j] > 0.40 and image_ndvi[i][j] <= 0.45:
            new_image[i, j, 1] = 200
            
        elif image_ndvi[i][j] > 0.45 and image_ndvi[i][j] <= 0.50:
            new_image[i, j, 1] = 255
        
        # Desmatamento
        elif image_ndvi[i][j] > 0.50 and image_ndvi[i][j] <= 0.55:
            new_image[i, j, 0] = 255 
            
        elif image_ndvi[i][j] > 0.50:
            new_image[i, j, 0] = 200 

# Plota a imagem
plt.imshow(new_image, cmap=None)