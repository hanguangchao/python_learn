#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:36:06 2019

@author: han
"""

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x = np.arange(-3*np.pi, 3*np.pi, 0.1)
    #print(x)

    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)
    y_arctan = np.arctan(x)
    y_arccos = np.arccos(x)

    plt.subplot(2, 3, 1)
    plt.plot(x, y_sin)
    plt.title('Sine')

    plt.subplot(2, 3, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')

    plt.subplot(2, 3, 3)
    plt.plot(x, y_tan)
    plt.title('Tan')

    plt.subplot(2, 3, 4)
    plt.plot(x, y_arctan)
    plt.title('Arttan')

    plt.subplot(2, 3, 5)
    plt.plot(x, y_arccos)
    plt.title('Arccos')
    plt.show()
