# -*- coding:utf-8 -*-
# 折线图
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties 

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 支持中文 
zhfont1 = FontProperties(fname='STHeiti Medium.ttc')
plt.title(u"Square Numbers实例", fontsize=24, fontproperties=zhfont1)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()
