from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Definir o caminho da imagem local
image_path = "./image-1.jpg"  # Substitua pelo caminho correto da sua imagem

# Carregar a imagem
img = Image.open(image_path)

# Carregar a imagem
plt.imshow(img)
plt.axis('off')  # Opcional: remove os eixos da imagem
plt.show()

# Converter para tons de cinza
img_gray = img.convert('L')

# Converter para preto e branco (threshold)
# Definindo o valor do limiar (threshold). O valor 128 é um bom valor (entre 0 e 255).
threshold = 128
img_bw = img_gray.point(lambda p: 255 if p > threshold else 0)


# Configurar a exibição das 3 imagens lado a lado
fig, axs = plt.subplots(1, 3, figsize=(15, 5))  # 1 linha e 3 colunas

# Exibir a imagem original
axs[0].imshow(img)
axs[0].axis('off')  # Remover os eixos
axs[0].set_title('Original')

# Exibir a imagem em tons de cinza
axs[1].imshow(img_gray, cmap='gray')
axs[1].axis('off')  # Remover os eixos
axs[1].set_title('Tons de Cinza')

# Exibir a imagem em preto e branco
axs[2].imshow(img_bw, cmap='gray')
axs[2].axis('off')  # Remover os eixos
axs[2].set_title('Preto e Branco')

# Exibir as imagens
plt.tight_layout()  # Ajusta o layout para não sobrepor as imagens
plt.show()