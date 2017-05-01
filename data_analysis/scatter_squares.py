# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
#y_values = [x**2 for x in x_values]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])
plt.show()
