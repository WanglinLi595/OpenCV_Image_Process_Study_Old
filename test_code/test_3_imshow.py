import cv2   

image = cv2.imread("../pic/lena512.bmp", cv2.IMREAD_UNCHANGED)     # 读取图片
cv2.imshow("Test_3", image)         # 开辟一个窗口显示图片
cv2.waitKey(0)                  # 等待用户按下按键
cv2.destroyAllWindows()         # 释放所有窗口