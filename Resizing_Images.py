import cv2
image1=cv2.imread("pineapple.jpg")
image2=cv2.imread("strawberry.jpg")
image3=cv2.imread("pomegranate.jpg")

cv2.namedWindow("Loaded Image 1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image 1", 200,200)
cv2.imshow("Loaded Image 1",image1)

cv2.namedWindow("Loaded Image 2", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image 2", 400,400)
cv2.imshow("Loaded Image 2",image2)

cv2.namedWindow("Loaded Image 3", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image 3", 600,600)
cv2.imshow("Loaded Image 3",image3)

key=cv2.waitKey(0)

if key == ord("s"):
    cv2.imwrite("Small_Img.jpg", image1)
    print("Image saved as Small_Img.jpg")
    cv2.imwrite("Medium_Img.jpg", image2)
    print("Image saved as Medium_Img.jpg")
    cv2.imwrite("Big_Img.jpg", image3)
    print("Image saved as Big_Img.jpg")
else:
    print("Images not saved.")

print(f"Image 1 Dimensions: {image1.shape}")
print(f"Image 2 Dimensions: {image2.shape}")
print(f"Image 3 Dimensions: {image3.shape}")