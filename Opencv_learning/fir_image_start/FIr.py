import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img = cv.imread('hello.jpg', 1)  # 0表示在加载灰度图像
# cv.imwrite('grad_hello.jpg', img)
# cv.imshow('image', img)
# cv.waitKey(0)  # 0 无线等待一个按键
# cv.destroyAllWindows()  # 销毁所有窗口


img = cv.imread('img/hello.jpg', 1)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()