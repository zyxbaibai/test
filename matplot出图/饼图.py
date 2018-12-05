# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

m = 50000
n = 40000

su_m = m/(m + n)
su_n = n/(m + n)

color_arr = ['navy','y']
label_arr = ['sua','sub']

plt.figure(figsize=(8,6))

# explode 缝隙间距
sua,sub,suc = plt.pie([su_m,su_n],labels=label_arr,autopct='%.1f%%',explode=[0,0.05],colors=color_arr)

# 修改字体大小
for i in sub + suc:
    i.set_fontsize(20)

# 修改 字体颜色
for i in suc:
    i.set_color('white')

plt.show()










































































































