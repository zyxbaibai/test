# -*- coding: utf-8 -*-
import numpy,random
import matplotlib.pyplot as plt


# with plt.xkcd():
#     data = numpy.random.normal(0,20,1000)
#     bins = numpy.arange(-100,100,5)
#
#     plt.hist(data,bins=bins) # hist直方图
#     plt.xlim([min(data)-5,max(data) + 5]) # 左右区间设置
#     plt.show()



# # 多直方图
# with plt.xkcd():
#     data1 = [random.gauss(15,10) for i in range(500)]
#     data2 = [random.gauss(5,5) for k in range(500)]
#     bins = numpy.arange(-50,50,2.5)
#
#     plt.hist(data1,bins=bins,alpha=0.3,label='sua') # 直方图
#     plt.hist(data2,bins=bins,alpha=0.3,label='sub') # 直方图
#     plt.legend(loc='best')  # 最佳位置 自动闪避
#
#     plt.show()



# # 散点图
# mu_ve = numpy.array([0,0])
# cov_ma = numpy.array([[2,0],[0,2]])
#
# sua = numpy.random.multivariate_normal(mu_ve,cov_ma,100)
# sub = numpy.random.multivariate_normal(mu_ve+0.2,cov_ma+0.2,100)
# suc = numpy.random.multivariate_normal(mu_ve+0.4,cov_ma+0.4,100)
#
# plt.figure(figsize=(8,6))
# plt.scatter(sua[:,0],sua[:,1],marker='x',color='blue',alpha=0.3,label='x1')
# plt.scatter(sub[:,0],sub[:,1],marker='h',color='red',alpha=0.3,label='x1')
# plt.scatter(suc[:,0],suc[:,1],marker='1',color='green',alpha=0.3,label='x1')
#
# plt.show()





# 散点图
x_data = numpy.random.rand(5)
y_data = numpy.random.rand(5)

plt.figure(figsize=(8,6))
plt.scatter(x_data,y_data,marker='h',s=50)

for x,y in zip(x_data,y_data):
    plt.annotate('(%.2f,%.2f)'%(x,y),xy=(x,y),xytext=(0,-15),textcoords='offset points',ha='center')

plt.show()
















































































