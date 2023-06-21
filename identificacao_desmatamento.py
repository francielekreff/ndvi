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
from matplotlib.patches import Patch

#Pré-processamento

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

# Carrega a imagem vermelha (RED) - Banda 7
image_red = cv2.imread('CBERS_4_MUX_20230520_178_104_L4_BAND7.tif', -1)

# Carrega a imagem infravermelha (NIR) - Banda 8
image_nir = cv2.imread('CBERS_4_MUX_20230520_178_104_L4_BAND8.tif', -1)

#plt.imshow(image_nir, cmap=None) # Imagem original NIR

# Rotaciona imagens
image_red = rotation(image_red)
image_nir = rotation(image_nir)

# Plota a imagem rotacionada
plt.imshow(image_nir, cmap=None)