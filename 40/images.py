import cv2
from PIL import Image
import numpy as np

#przygotowanie funkcji do wyświetlania obrazu za pomocą biblioteki opencv
def show_image(img):
	cv2.imshow("image", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#przygotowanie funkcji, która wczyta obraz z pliku za pomocą biblioteki opencv, a później go wyświetli
def read_image_opencv(path):
	img = cv2.imread(path, cv2.IMREAD_COLOR)
	print(img)
	print(img.shape)
	print(type(img))
	show_image(img)
	return img

image = read_image_opencv("image.jpg")
read_image_opencv("image.jpg")

#przygotowanie funkcji, która wczyta obraz z pliku za pomocą biblioteki pillow, a później go wyświetli
def read_image_pillow(path):
	img = Image.open("image.jpg")
	try:
		print(img)
	except:
		print(type(img))
	img.show()
	return img

read_image_pillow("image.jpg")

#obracanie obrazu piksel po pikselu, czyli przenoszenie elementów z końca tablicy na początek
#przechodzimy przez wszystkie rzędy, a następnie dla każdego rzędu przepisujemy piksele w odwrotnej kolejności
#(z tej samej kolumny, ale rząd bierzemy od dołu zamiast od góry)

def reverse_image(img):
	new_img = []
	for row in range(img.shape[0]):
		new_row = []
		for column in range(img.shape[1]):
			new_row.append(img[-1-row][column])
		new_img.append(new_row)
	return np.array(new_img)


show_image(reverse_image(image))

#odwracanie obrazu, ale za pomocą wycinków list

def reverse_image_short(img):
	img_reverse = img[::-1]
	return img_reverse

show_image(reverse_image_short(image))

#to samo ale wbudowaną funkcją w opencv
show_image(cv2.flip(image, 0))

#zamiana koloru na skalę szarości
def gray_scale(img):
	for row in range(img.shape[0]):
		for column in range(img.shape[1]):
			gray = int(sum(img[row][column]/3))
			img[row][column][0] = gray
			img[row][column][1] = gray
			img[row][column][2] = gray
	return np.array(img)

show_image(gray_scale(image))

#to samo ale wbudowaną funkcją w opencv
show_image(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

#filtr sepia - ciepły ton, przypominający stare fotografie
def sepia(img):
	for row in range(img.shape[0]):
		for column in range(img.shape[1]):
			B = img[row][column][0]
			G = img[row][column][1]
			R = img[row][column][2]
			img[row][column][2] = min(255, (0.393*R + 0.769*G + 0.189*B))
			img[row][column][1] = min(255, (0.349*R + 0.686*G + 0.168*B))
			img[row][column][0] = min(255, (0.272*R + 0.534*G + 0.131*B))
	return np.array(img, dtype= np.uint8)

show_image(sepia(image))
