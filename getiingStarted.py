# Importing OpenCV
import cv2

# Reading image, 1 for original, 0 for gray scale, -1 for original.....
img =cv2.imread('lena.jpg', 1)
# printing the image matrix
print(img)

# displaying images
cv2.imshow('image', img)

#  Capturing Key uptill 5 sec
k = cv2.waitKey(5000)

# if key is escape destroy the opened window
if(k==27):
    cv2.destroyAllWindows()
# if key is s save and then destroy the window, ord fun returns the key value
elif(k == ord('s')):
    cv2.imwrite('lena_copy.jpg', img)
    cv2.destroyAllWindows()