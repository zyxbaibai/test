# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt



# with plt.xkcd():
#     numpy.random.seed(0)
#     x = numpy.arange(5)
#     y = numpy.random.randn(5)
#     plt.bar(x,y)  # bar 是条形图
#     plt.show()




# with plt.xkcd():
#     numpy.random.seed(0)
#     x = numpy.arange(5)
#     y = numpy.random.randn(5)
#     plt.barh(x,y)  # barh 是横向条形图
#     plt.show()



# # 条形图 子图
# numpy.random.seed(0)
# x = numpy.arange(5)
# y = numpy.random.randn(5)
# # subplots 子图
# sua,sub = plt.subplots(ncols=2)
# sub[0].bar(x,y)
# sub[1].barh(x,y)
# plt.show()



# # 正负水平线
# numpy.random.seed(0)
# x = numpy.arange(5)
# y = numpy.random.randint(-5,5,5)
# plt.bar(x,y)
# plt.axhline(0,color='r',linewidth=2)  # x=0 的一条线
# plt.show()



# # 负值变色
# numpy.random.seed(0)
# x = numpy.arange(5)
# y = numpy.random.randint(-5,5,5)
# sua,sub = plt.subplots()
#
# v_bars = sub.bar(x,y)
# for bar,height in zip(v_bars,y):
#     if height < 0:
#         bar.set(color='c')
#
# plt.axhline(0,color='r',linewidth=2)  # x=0 的一条线
# plt.show()


# # 填充图    cumsum 累加和 每一个位置值等于之前所有值之和
# with plt.xkcd():
#     x = numpy.random.randn(100).cumsum()
#     y = numpy.linspace(0,10,100)
#     sua,sub = plt.subplots()
#     sub.fill_between(x,y)
#     plt.show()



# # 填充折线图
# with plt.xkcd():
#     x = numpy.linspace(0,10,200)
#     y1 = 2*x + 1
#     y2 = 3*x + 1.5
#     y_mean = 0.5*x*numpy.cos(2*x) + 2.5*x + 1.1
#
#     sua,sub = plt.subplots()
#     sub.fill_between(x,y1,y2,color='c')
#     sub.plot(x,y_mean,color='#ff00ff')
#     plt.show()


# # 误差棒
# mean_values = [1,2,3]
# variance = [0.2,0.4,0.5]
# bar_label = ['bar1','bar2','bar3']
#
# x_pos = list(range(len(bar_label)))
# plt.bar(x_pos,mean_values,yerr=variance) # yerr 误差棒
# max_y = max(zip(mean_values,variance))
#
# plt.ylim([0,(max_y[0] + max_y[1]) * 1.2]) # 限制（浮动范围）
# plt.ylabel('variance_y')
# plt.xticks(x_pos,bar_label)
# plt.show()



# # 背靠背图
# x1 = numpy.array([1,2,3])
# x2 = numpy.array([2,2,3])
#
# bar_labels = ['bar1','bar2','bar3']
# fig = plt.figure(figsize=(8,6))  # 画布分辨率
# y_pos = numpy.arange(len(x1))
# x_pos = [x for x in y_pos]
#
# plt.barh(y_pos,x1,color='c',alpha=0.5)  # 正向条形图 alpha透明度
# plt.barh(y_pos,-x2,color='b',alpha=0.5) # 反向条形图
#
# plt.xlim(-max(x2) - 1,max(x1) + 1)  # x边距设置
# plt.ylim(-1,len(x1) + 1)  # y边距设置
# plt.show()



# # 多柱图
# green_data = [1,2,3]
# blue_data = [3,2,1]
# red_data = [2,3,3]
# labels = ['group1','group2','group3']
#
# pos = list(range(len(green_data)))
# width = 0.2
# fig,ax = plt.subplots(figsize=(8,6))
# plt.bar(pos,green_data,width,color='c',label=labels[0])
# plt.bar([i + width for i in pos],blue_data,width,color='b',label=labels[0])
# plt.bar([i + width*2 for i in pos],red_data,width,color='r',label=labels[0])
# plt.show()



# # 条形图 标注
# data = range(200,225,5)
# labels = ['a','b','c','d','e']
# fig = plt.figure(figsize=(8,6))
# y_pos = numpy.arange(len(data))
# plt.yticks(y_pos,labels,fontsize=16)
# bars = plt.barh(y_pos,data,alpha=0.5,color='b')
# plt.vlines(min(data),-1,len(data) + 0.5,linestyles='--')
#
# # 设置备注
# for b,d in zip(bars,data):
#     plt.text(b.get_width() + b.get_width()*0.05,b.get_y() + b.get_height()/2,'{0:.2%}'.format(d/min(data)))
#
# plt.show()



# 风格 填充
patterns = ('-','+','x','\\','*','o','0','.')
fig = plt.gca()
mean_value = range(1,len(patterns) + 1)
x_pos = list(range(len(mean_value)))
bars = plt.bar(x_pos,mean_value,color='c')
for bar, pattern in zip(bars,patterns):
    bar.set_hatch(pattern)

plt.show()






