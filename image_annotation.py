import cv2
import matplotlib.pyplot as plt

image_path='fruits.jpg'
image=cv2.imread(image_path)
height, width, _=image.shape
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

thickness = 3
y_pos=height//2
cv2.arrowedLine(image_rgb,(20, y_pos),(width - 20, y_pos),(0, 255, 0),thickness,tipLength=0.05)
cv2.arrowedLine(image,(width - 20, y_pos + 30),(20, y_pos + 30),(0, 255, 0),thickness,tipLength=0.05)

text_x = width // 2 - 100
text_y = y_pos - 20
label=f"Width: {width} "
cv2.putText(image,label,(text_x, text_y),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0),2)

plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.title("Annotated Image")
plt.axis("off")