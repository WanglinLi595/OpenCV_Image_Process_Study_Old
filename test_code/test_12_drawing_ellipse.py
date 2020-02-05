#!/usr/bin/env python
# coding=utf-8
'''
@描述: 
@版本: V1_0
@作者: LiWanglin
@创建时间: Do not edit
@最后编辑人: LiWanglin
@最后编辑时间: Do not Edit
'''

import cv2 as cv
import numpy as np

# 创建一个黑色图框
img = np.zeros((512,512,3), np.uint8)

# 绘制一个红色的圆
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

cv.imshow("ellipse", img)         # 显示图片

cv.waitKey(0)

cv.destroyAllWindows()
