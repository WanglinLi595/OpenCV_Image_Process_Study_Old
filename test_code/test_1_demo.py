#!/usr/bin/env python
# coding=utf-8
'''
@描述: 
@版本: V1_0_0
@作者: LiWanglin
@创建时间: 2019.12.27
@最后编辑人: LiWanglin
@最后编辑时间: 2019.12.27
'''

import cv2      # 导入 OpenCV 模块

image = cv2.imread("../pic/lenacolor.png", cv2.IMREAD_UNCHANGED)   # 读取图片
cv2.imshow("Demo1", image)      # 显示图片
cv2.waitKey(0)                  # 等待用户按下按键
cv2.destroyAllWindows()         # 释放所有窗口