import cv2      # 导入Opencv模块

image = cv2.imread("../pic/lenacolor.png", cv2.IMREAD_UNCHANGED)   # 读取图片
cv2.imshow("Demo1", image)      # 显示图片
cv2.waitKey(0)                  # 等待用户按下按键
cv2.destroyAllWindows()         # 释放所有窗口