import cv2
import numpy as np

img = np.zeros((200, 300, 3), np.uint8)
cv2.circle(img, (150, 100), 50, (0, 255, 0), -1)
cv2.imwrite("test.png", img)
print("opencv:", cv2.__version__, "/ numpy:", np.__version__)
