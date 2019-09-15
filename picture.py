import cv2
import matplotlib.pyplot as plt
import numpy as np
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
img=cv2.imread("pic.jpg")
##通过opencv显示图像
# cv2.imshow("img",img)
# cv2.waitKey(0)
#plt.imshow是对图像进行处理并显示格式
plt.imshow(img)
#plt.show是显示经过plt.imshow处理后的图像
plt.show()
##利用cvtcolor函数显示灰度图
# imgray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#利用自定义函数显示灰度图
imgray=rgb2gray(img)
plt.imshow(imgray)
plt.show()