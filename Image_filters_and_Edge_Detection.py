import cv2
import numpy as np

image = cv2.imread("pineapple.jpg")

if image is None:
    print("Error: Could not load image.")
    exit()

current_image = image.copy()

print("Controls:")
print("r - Red channel")
print("g - Green channel")
print("b - Blue channel")
print("s - Sobel Edge Detection")
print("c - Canny Edge Detection")
print("o - Original Image")
print("q - Quit")

while True:
    cv2.imshow("Image Processing", current_image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('o'):
        current_image = image.copy()

    elif key == ord('r'):
        red = image.copy()
        red[:, :, 0] = 0      
        red[:, :, 1] = 0      
        current_image = red

    elif key == ord('g'):
        green = image.copy()
        green[:, :, 0] = 0    
        green[:, :, 2] = 0    
        current_image = green

    elif key == ord('b'):
        blue = image.copy()
        blue[:, :, 1] = 0     
        blue[:, :, 2] = 0     
        current_image = blue


    elif key == ord('s'):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel = cv2.magnitude(sobelx, sobely)
        sobel = np.uint8(np.clip(sobel, 0, 255))
        current_image = sobel

    elif key == ord('c'):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        current_image = edges

    elif key == ord('q'):
        print("Exiting")
        break

    else:
        print("Invalid Input. Use r, g, b, s, c, o, or q.")

cv2.destroyAllWindows()