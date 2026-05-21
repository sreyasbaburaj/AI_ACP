import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("strawberry.jpg")

gray_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img)
plt.title("Grayscale Image")
plt.show()

crop_img=image[100:300,200:400]
crop_rgb=cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
plt.imshow(crop_rgb)
plt.title("Cropped Image")
plt.show()

height,width=image.shape[0:2]
rotated_matrix=cv2.getRotatedMatrix2D(center=(width/2,height/2), angle=45, scale=1)
rotated_img = cv2.warpAffine(src=image, M=rotated_matrix, dsize=(width, height))
rotate_rgb=cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB)
plt.imshow(rotate_rgb)
plt.title("Rotated Image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype=np.uint8)*50
bright_img=cv2.add(image, brightness_matrix)
bright_rgb=cv2.cvtColor(bright_img, cv2.COLOR_BGR2RGB)
plt.imshow(bright_rgb)
plt.title("Bright Image")
plt.show()