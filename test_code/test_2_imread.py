import cv2   

image = cv2.imread("../pic/lena512.bmp", cv2.IMREAD_UNCHANGED)     # 读取图片
print("image的类型为：" , type(image))              # 打印图片类型
print("image = \n" , image)                        # 打印图片数据