# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt


# # 盒图 箱型图
# arr = [numpy.random.normal(0,i,100) for i in range(1,4)]
# fig = plt.figure(figsize=(8,6))
# plt.boxplot(arr,notch=False,sym='s',vert=True)
# plt.xticks([i+1 for i in range(len(arr))],['x1','x2','x3']) # 注释
# plt.show()



# # 盒图颜色
# arr = [numpy.random.normal(0,i,100) for i in range(1,4)]
# fig = plt.figure(figsize=(8,6))
# bp_lot = plt.boxplot(arr,notch=False,sym='s',vert=True)
# plt.xticks([i+1 for i in range(len(arr))],['x1','x2','x3']) # 注释
#
# # 颜色
# for components in bp_lot.keys():
#     for line in bp_lot[components]:
#         line.set_color('y')
#
# plt.show()




# # 盒图横向
# arr = [numpy.random.normal(0,i,100) for i in range(1,4)]
# fig = plt.figure(figsize=(8,6))
# bp_lot = plt.boxplot(arr,notch=False,sym='s',vert=False)  # vert横向
# plt.xticks([i+1 for i in range(len(arr))],['x1','x2','x3']) # 注释
#
# # 颜色
# for components in bp_lot.keys():
#     for line in bp_lot[components]:
#         line.set_color('y')
#
# plt.show()




# # 盒图凹形
# arr = [numpy.random.normal(0,i,100) for i in range(1,4)]
# fig = plt.figure(figsize=(8,6))
# bp_lot = plt.boxplot(arr,notch=True,sym='s',vert=False)  # vert横向 notch凹形
# plt.yticks([i+1 for i in range(len(arr))],['x1','x2','x3']) # 注释
#
# # 颜色
# for components in bp_lot.keys():
#     for line in bp_lot[components]:
#         line.set_color('y')
#
# plt.show()





# # 盒图 填充色
# arr = [numpy.random.normal(0,i,100) for i in range(1,4)]
# fig = plt.figure(figsize=(8,6))
# # vert横向 notch凹形   patch_artist 填充色
# bp_lot = plt.boxplot(arr,notch=False,sym='s',vert=True,patch_artist=True)
# plt.yticks([i+1 for i in range(len(arr))],['x1','x2','x3']) # 注释
#
# # 颜色
# colors = ['pink','lightblue','lightgreen']
# for patch,color in zip(bp_lot['boxes'],colors):
#     patch.set_facecolor(color)
#
# plt.show()





# 小提琴图
fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(8,6))

arr = [numpy.random.normal(0,i,100) for i in range(6,10)]
ax[0].violinplot(arr,showmeans=False,showmedians=True) # 小提琴图
ax[1].boxplot(arr) # 盒图

# 水平线
for i in ax:
    i.yaxis.grid(True)
    i.set_xticks([y+1 for y in range(len(arr))])

plt.show()





















































