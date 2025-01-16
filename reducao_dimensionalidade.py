from PIL import Image

# Converter para tons de cinza manualmente
def rgb_to_gray(r, g, b):
    # Fórmula simples de conversão para tons de cinza (média ponderada)
    return int(0.299 * r + 0.587 * g + 0.114 * b)
# Converter para preto e branco (usando um threshold de 128)
def rgb_to_bw(gray_value, threshold=128):
    return 255 if gray_value > threshold else 0

# Abrir a imagem
image_path = './image-1.jpg'  # Caminho da sua imagem
img = Image.open(image_path)

# Converter a imagem para tons de cinza
width, height = img.size
img_gray = Image.new("L", (width, height))  # Nova imagem em tons de cinza

pixels = img.load()  # Carrega os pixels da imagem original
pixels_gray = img_gray.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        gray = rgb_to_gray(r, g, b)
        pixels_gray[i, j] = gray


# Converter para preto e branco
img_bw = Image.new("1", (width, height))  # Nova imagem binária (preto e branco)
pixels_bw = img_bw.load()

for i in range(width):
    for j in range(height):
        gray = pixels_gray[i, j]
        bw = rgb_to_bw(gray)
        pixels_bw[i, j] = bw

# Definindo o espaço entre as imagens
space = 10  # Espaço de 10 pixels entre as imagens

# Criar uma nova imagem com espaço extra para as 3 imagens e o espaço entre elas
combined_width = width * 3 + space * 2  # Espaço extra entre as imagens
combined_image = Image.new("RGB", (combined_width, height), (255, 255, 255))  # Fundo branco

# Colocar as imagens na nova imagem com o espaço entre elas
combined_image.paste(img, (0, 0))  # A imagem original vai para a primeira posição
combined_image.paste(img_gray.convert("RGB"), (width + space, 0))  # A imagem em tons de cinza vai para a segunda
combined_image.paste(img_bw.convert("RGB"), (2 * width + 2 * space, 0))  # A imagem preto e branco vai para a terceira

# Exibir a imagem combinada
combined_image.show()
