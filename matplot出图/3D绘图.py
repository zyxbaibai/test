# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



# # 3d 绘图
# fig = plt.figure()  # 画布
# ax = Axes3D(fig)
#
# x = numpy.arange(-4,4,0.25)
# y = numpy.arange(-4,4,0.25)
# x,y = numpy.meshgrid(x,y)
# r = numpy.sqrt(x**2+y**2)
# z = numpy.sin(r)
#
# # 高度
# ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap='rainbow')
#
# # ax.contourf(x,y,z,zdir='z',offset=-2,cmap='rainbow') # zdir表示对应轴投影
# # ax.view_init()
# plt.show()



# # 3d 结构 =================
# fig = plt.figure()
#
# ax = fig.add_subplot(111,projection="3d")
#
# plt.show()



# # 3d 线圈 ================================================
#
# fig = plt.figure()
# ax = fig.gca(projection="3d")
#
# sua = numpy.linspace(-4 * numpy.pi, 4*numpy.pi ,100)
# z = numpy.linspace(-2,2,100)
# r = z ** 2+1
# x = r * numpy.sin(sua)
# y = r * numpy.cos(sua)
# ax.plot(x,y,z,color="r")
# plt.show()




# 3d 散点图 ===============================================
# numpy.random.seed(19)
# def range_action(n,vmin,vmax):
#     return (vmax-vmin)*numpy.random.rand(n)+vmin
#
# fig = plt.figure()
# ax = fig.add_subplot(111,projection="3d")
# n = 100
# for c,m,z_low,z_high in [("r","o",-50,-25),("b","x","-30","-5")]:
#     xs = range_action(n,23,32)
#     ys =  range_action(n,0,100)
#     zs = range_action(n,int(z_low),int(z_high))
#     ax.scatter(xs,ys,zs,marker=m) # 散点图
#
# # ax.view_init(30,0) # 初始化角度
# plt.show()



# 3d 直方图 ================================================

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

for c,z in zip(["r","g","b","y"],[30,20,10,0]):
    xs = numpy.arange(20)
    ys = numpy.random.rand(20)
    cs = [c]*len(xs)
    ax.bar(xs,ys,zs=z,zdir="y",color=cs,alpha=0.5)

plt.show()












































































