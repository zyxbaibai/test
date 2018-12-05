# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt



# # 卡通线条
# with plt.xkcd():
#     arr = [1,2,3,4,5]
#     arr1 = np.array(arr)
#     # marker 关键点
#     plt.plot(arr1,arr1**4,'#FF00FF',linestyle='-.',marker='h')
#     plt.ylabel('y')
#     plt.show()




# # 多线条
# with plt.xkcd():
#     n = np.arange(10)
#     plt.plot(n,n,'#FF00FF',
#              n,n**2,'b',
#              n,n**3,'g')
#     plt.show()



# # 关键点
# with plt.xkcd():
#     x = np.linspace(-10,10)
#     y = np.sin(x)
#     plt.plot(x,y,linestyle='-.',marker='h',markerfacecolor='#ff00ff',markersize='8')
#     plt.title('标题', fontproperties='STCaiyun')  # 标题
#     plt.show()



# # 单独设置样式
# with plt.xkcd():
#     x = np.linspace(-10,10)
#     y = np.sin(x)
#     sua = plt.plot(x,y)
#     # alpha 透明度
#     plt.setp(sua,color='r',linewidth=2.0,alpha=0.5)
#     plt.show()



# # 两行一列
# with plt.xkcd():
#     x = np.linspace(-10,10)
#     y = np.sin(x)
#     # 两行一列 第一个子图
#     plt.subplot(211) # 211意思为 2行1列占第一个坑
#     plt.plot(x,y,'#ff00ff')
#     # 两行一列 第二个子图
#     plt.subplot(212) # 211意思为 2行1列占第二个坑
#     plt.plot(x,y,color='g')
#
#     plt.show()



# # 一行两列
# with plt.xkcd():
#     x = np.linspace(-10,10)
#     y = np.sin(x)
#     # 两行一列 第一个子图
#     plt.subplot(121) # 121意思为 1行2列占第一个坑
#     plt.plot(x,y,'#ff00ff')
#     # 两行一列 第二个子图
#     plt.subplot(122) # 122意思为 1行2列占第二个坑
#     plt.plot(x,y,color='g')
#
#     plt.show()



# 箭头
with plt.xkcd():
    x = np.linspace(-10,10)
    y = np.sin(x)
    plt.plot(x,y,marker='h',markerfacecolor='#ff00ff',markersize='8')
    plt.title('标题',fontproperties='STCaiyun')   # 标题汉字
    # (0,0) 文本在坐标系坐标
    plt.text(0,0,'百货桑',fontproperties='STXihei') # 坐标文本 汉字
    plt.grid(True)  # 背景带网格
    # facecolor箭头本体颜色   shrink箭头尾部距离xytext的距离
    # headwidth箭'头'的宽  headlength箭'头'的长
    dic = dict(facecolor='r',shrink=0.05,headwidth=10,headlength=10)  # shrink标注与箭头距离
    # xy=(-5,0)箭头位置   xytext=(2,0.5) 箭头尾部位置  sugar在xytext位置
    plt.annotate('sugar',xy=(-5,0),xytext=(2,0.5),arrowprops=dic) # 箭头

    plt.show()

























































































