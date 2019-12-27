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

import cv2   

image = cv2.imread("../pic/lena512.bmp", cv2.IMREAD_UNCHANGED)     # 读取图片
print("image的类型为：" , type(image))              # 打印图片类型
print("image = \n" , image)                        # 打印图片数据