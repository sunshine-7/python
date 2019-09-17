# import base64
# import cv2
# from matplotlib import pyplot as plt
# import numpy as np
# #RGB到灰度图转换公式：Y' = 0.299 R + 0.587 G + 0.114 B
# def rgb2gray(rgb):
#     #dot，类似于矩阵相乘
#     return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
# img=cv2.imread("pic.jpg")
# # cv2.imread("",flags)
# # flags = -1：imread按解码得到的方式读入图像
# # flags = 0：imread按单通道的方式读入图像，即灰白图像
# # flags = 1：imread按三通道方式读入图像，即彩色图像
# ##通过opencv显示图像
# # cv2.imshow("img",img)
# # #等待x ms，如果在此期间有按键按下，则立即结束并返回按下按键的ASCII码，否则返回-1
# # # 如果x=0，那么无限等待下去，直到有按键按下
# # cv2.waitKey(0)
# #plt.imshow是对图像进行处理并显示格式
# plt.imshow(img)
# #plt.show是显示经过plt.imshow处理后的图像
# plt.show()
# ##利用cvtcolor函数显示灰度图
# # imgray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# #利用自定义函数显示灰度图
# imgray=rgb2gray(img)
# plt.imshow(imgray)
# plt.show()
# # base64.b64encode(s[, altchars])
# # base64.b64decode(s[, altchars])
# # altchars为可选的参数，用来替换+和/的一个两个长度的字符串。
# #base64.urlsafe_b64encode(s)
# # base64.urlsafe_b64decode(s)
# # 此方法中用-代替了+，用_代替了/，这样可以保证编码后的字符串放在url里可以正常访问
# #base64加密：base64.b64encode(XXX)
# imgray_cip=base64.urlsafe_b64encode(imgray)
# #imgray_cip是字符串，所以不能用cv2.imshow
# #base64解密：base64.b64decode(base64.b64encode(XXX))
# imgray_laws=base64.urlsafe_b64decode(imgray_cip)
# plt.imshow(imgray_laws)
# plt.show()



#by hgg
import base64
import cv2
from matplotlib import pyplot as plt
import numpy as np
#RGB到灰度图转换公式：Y' = 0.299 R + 0.587 G + 0.114 B
def rgb2gray(rgb):
    #dot，类似于矩阵相乘
    #----------rgb[...,:3]
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
#表示将整个图像窗口分为1行2列, 当前位置为1.
# 其中各个参数也可以用逗号，分隔开。
# 第一个参数代表子图的行数；第二个参数代表该行图像的列数；
# 第三个参数代表每行的第几个图像。
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
#imgray.shape表示图片的高度、宽度、通道数
print(imgray.shape)
# '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样
# cv2.imencode()函数是将图片格式转换(编码)成流数据，赋值到内存缓存中;
# 主要用于图像数据格式的压缩，方便网络传输.
#将灰度图转换成数组存进内存，变量imgEncode指向该内存地址
#图片，数组，字符串，加密，解密，数组，图片
imgEncode = cv2.imencode(".jpg", imgray)[1]
#np.array的作用：将数组[[1,2],[4,5],[3,6]]转换成
# [[1 2]
#  [4 5]
#  [3 6]]的格式输出
#np.array(imgEncode).tostring()将图片转换成的数组转换成字符串
#base64.b64encode：将字符串加密
imgBase64Str = base64.b64encode(np.array(imgEncode).tostring())

#对字符串解密
tImg = base64.b64decode(imgBase64Str)
#np.fromstring(tImg, dtype='uint8')将解密后的字符串转换成数组
# cv2.imdecode()从指定的内存缓存中读取数据，并把数据转换(解码)成图像格式;
# 主要用于从网络传输数据中恢复出图像。
# uint8是无符号八位整型，表示范围是[0, 255]的整数
tImg = cv2.imdecode(np.fromstring(tImg, dtype='uint8'),1)
print(tImg.shape)    #注意转换前后的矩阵的维数   输入通道是（500， 600），输出变成了（500， 600， 3）
#查一下图的表示方法
plt.imshow(tImg)
plt.show()


