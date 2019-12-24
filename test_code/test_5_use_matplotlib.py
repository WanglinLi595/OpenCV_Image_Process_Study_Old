import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("pic/lena512.bmp", cv.IMREAD_UNCHANGED) # 读取图片
# 设置图片在 matplotlib 的显示方式
plt.imshow(img, cmap="gray", interpolation='bicubic')
plt.show()          # 显示图像