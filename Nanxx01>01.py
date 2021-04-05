import cv2
import numpy as np
import matplotlib as plt
import os


img = cv.imread('pic.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27:
     cv.destroyAllWindows()
 elif k == ord('s'):
     cv.imwrite('pic.jpg',img)
     cv.destroyAllWindows()
