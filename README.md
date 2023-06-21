# Identificação de Áreas de Desmatamento Utilizando NDVI

Um dos primeiros passos a ser realizado no combate ao desmatamento é a criação de metodologias e técnicas que possibilitem monitorar áreas de desmatamento em grandes biomas, como o bioma amazônico, de forma eficiente e com custo razoável.

As imagens de sensoriamento remoto são amplamente utilizadas para fazer esse monitoramento, pois representam uma fonte de dados atualizada sistematicamente e capaz de abranger grandes extensões.

O projeto tem como objetivo desenvolver uma metodologia de processamento de imagem para a identificação de áreas de desmatamento, a partir de imagens de sensoriamento remoto, OpenCV, Python e o Índice de Vegetação de Diferença Normalizada (NDVI).

O projeto foi divido nas estapas de aquisição de images, pré-processamento, processamento por meio de NDVI e desenvolvimento do mapa de NDVI.


### Aquisição de Imagens

As imagens foram adquiridas do catálogo de imagens do INPE/OBT (Instituto Nacional de Pesquisas Espaciais/Divisão de Geração de Imagens) e são provenientes do satélite CBERS-4.

As imagens foram capturadas com a câmera multiespectral MUX, a qual cobre as quatro faixas espectrais: B (_blue_) - faixa azul, G (_green_) - faixa verde, R (_red_) - faixa vermelha e NIR - infravermelho. A câmera MUX do satélite CBERS-4 possui de resolução espacial de 20 metros e largura de faixa da imagem de 120 km. 

A região escolhida para análise deste trabalho está localiza no estado do Amazonas, em uma área que cobre o rio Tefé e sua imagem RGB pode ser visualizada na figura abaixo:  

<img src="https://github.com/francielekreff/ndvi/blob/main/imagens/CBERS_4_MUX_20230520_178_104.png" width="400">

Ao realizar o download das imagens no catálogo de imagens do INPE/OBT são obtidas quatro imagens, uma de cada faixa do espectro conforme citado anteriormente. As mesmas se encontram disponíveis através deste [link](https://drive.google.com/drive/folders/1nn0_0md1f75e2d5ojl8orLEUb_0FEV9u?usp=sharing). 


### Pré-Processamento

Em cada uma das imagens (B, G, R e NIR) obtidas, foi realizada a técnica de rotação, que permitiu rotacionar a imagem em um ângulo de 8,53º, correspondente a rotação da imagem gerada pelo satélite CBERS-4.

Com a finalidade de analisar uma região com a presença de desmatamento e sem a interferência de nuvens, realizou-se o recorte em cada uma das imagens originais (B, G, R e NIR).


### NDVI e Mapa de NDVI

A página [NDVI](https://github.com/francielekreff/ndvi/wiki/NDVI) da Wiki apresenta uma breve descrição sobre o NDVI e sobre a obtenção de mapas de NDVI.


### Resultados

O resultado obtido através da etapa de pré-processamento da imagem NIR se encontra na figura abaixo.

![Imagem NIR Após Pré-Processamento](https://github.com/francielekreff/ndvi/blob/main/imagens/imagem_nir_recorte.png)

E o resultado final obtido através do mapa de NDVI se encontra na figura abaixo.

![Imagem Final](https://github.com/francielekreff/ndvi/blob/main/imagens/imagem_mapa_ndvi.png)
