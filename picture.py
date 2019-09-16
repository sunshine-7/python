import base64
import cv2
from matplotlib import pyplot as plt
import numpy as np
#RGB到灰度图转换公式：Y' = 0.299 R + 0.587 G + 0.114 B
def rgb2gray(rgb):
    #dot，类似于矩阵相乘
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
img=cv2.imread("pic.jpg")
# cv2.imread("",flags)
# flags = -1：imread按解码得到的方式读入图像
# flags = 0：imread按单通道的方式读入图像，即灰白图像
# flags = 1：imread按三通道方式读入图像，即彩色图像
##通过opencv显示图像
# cv2.imshow("img",img)
# #等待x ms，如果在此期间有按键按下，则立即结束并返回按下按键的ASCII码，否则返回-1
# # 如果x=0，那么无限等待下去，直到有按键按下
# cv2.waitKey(0)
#plt.imshow是对图像进行处理并显示格式
# plt.imshow(img)
# #plt.show是显示经过plt.imshow处理后的图像
# plt.show()
##利用cvtcolor函数显示灰度图
imgray1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#利用自定义函数显示灰度图
imgray=rgb2gray(img)
# diff = np.sum(imgray1 - imgray)
# print(diff)
# plt.subplot(121),plt.imshow(imgray1)
# plt.subplot(122),plt.imshow(imgray)
# # plt.imshow(imgray)
# plt.show()
#base64加密：base64.b64encode(XXX)
# imgray_cip=base64.urlsafe_b64encode(imgray)
# #imgray_cip是字符串，所以不能用cv2.imshow
# print(imgray_cip)
# #base64解密：base64.b64decode(base64.b64encode(XXX))
# imgray_laws=base64.urlsafe_b64decode(imgray_cip)
# plt.imshow(imgray)
# plt.show()

print(imgray.shape)
imgEncode = cv2.imencode(".jpg", imgray)[1]
imgBase64Str = base64.b64encode(np.array(imgEncode).tostring())

tImg = base64.b64decode(imgBase64Str)
tImg = cv2.imdecode(np.fromstring(tImg, dtype='uint8'), 1)
print(tImg.shape)    #注意转换前后的矩阵的维数   输入通道是（500， 600），输出变成了（500， 600， 3）
#查一下图的表示方法
plt.imshow(tImg)
plt.show()
