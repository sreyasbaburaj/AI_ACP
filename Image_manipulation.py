import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "strawberry.jpg"  
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(6, 6))
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

cropped_img=image[100:200,200:400]
cropped_rgb=cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.show()

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
rotated_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(6, 6))
plt.imshow(rotated_rgb)
plt.title("Rotated Image (45°)")
plt.axis("off")
plt.show()

brightened_image = cv2.convertScaleAbs(image,alpha=1,beta=50)

brightened_rgb = cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(6, 6))
plt.imshow(brightened_rgb)
plt.title("Brightened Image")
plt.axis("off")
plt.show()

cv2.imwrite("grayscale.jpg", gray_img)
cv2.imwrite("cropped.jpg",cv2.cvtColor(cropped_rgb, cv2.COLOR_RGB2BGR))
cv2.imwrite("rotated.jpg", rotated_image)
cv2.imwrite("brightened.jpg", brightened_image)

print("All images have been saved.")