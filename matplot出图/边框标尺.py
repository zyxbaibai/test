# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt
import math
# 移除标尺
# x = range(10)
# y = range(10)
#
# fig =plt.gca()
# plt.plot(x,y)
#
# fig.axes.get_xaxis().set_visible(False) # 移除x刻度
# fig.axes.get_yaxis().set_visible(False) # 移除y刻度
# plt.show()



# # 移除边框
# x = numpy.random.normal(loc=0,scale=1.0,size=300)
# width = 0.5
# bins = numpy.arange(math.floor(x.min())-width,math.ceil(x.min())+width,width)
# ax = plt.subplot(111)
# ax.spines['top'].set_visible(False) # 上边框不可见
# ax.spines['right'].set_visible(False) # 有边框不可见
# plt.tick_params(bottom='off',top='off',left='off',right='off') # 关闭标尺刻度
# # fig =plt.gca()
# # fig.axes.get_xaxis().set_visible(False) # 移除x刻度
# # fig.axes.get_yaxis().set_visible(False) # 移除y刻度
# plt.grid()  # 网格
# plt.hist(x,) # 直方图
# plt.show()



# # 批注设置
# x = range(10)
# y = range(10)
#
# label_arr = ['x%s'%i for i in range(10)]
# fig,ax = plt.subplots()
# plt.plot(x,y)
# # horizontalalignment 对齐
# ax.set_xticklabels(label_arr,rotation=45,horizontalalignment='right') # 批注角度
# plt.show()


# 提示器
x = numpy.arange(10)

for i in range(1,4):
    plt.plot(x,i*x**2,label='group%s'%i)

plt.legend(loc='best',framealpha=0.1)  # 提示器 best自动位置
plt.show()































































































