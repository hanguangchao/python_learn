#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:24:56 2019

@author: han
"""

import math


class Vector:
    #构造方法，传进来的是一个lst数组  
    def __init__(self,lst):
        self._values=lst
        
    def __add__(self, another):
        """向量加法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."

        # return Vector([a + b for a, b in zip(self._values, another._values)])
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        """向量减法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in subtracting. Length of vectors must be same."
            
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        """返回数量乘法的结果向量：self * k"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回数量乘法的结果向量：k * self"""
        return self * k
    
    def __truediv__(self, k):
        """返回数量除法的结果向量：self / k"""
        return (1 / k) * self

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()
    #供系统调用的魔法方法
    def __repr__(self):
        return "Vector({})".format(self._values)

    #相当于Java的toString方法，用户调用
    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))

    #返回向量的维度
    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    #返回向量中第第index元素
    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]
    

    
    @classmethod
    def zero(cls, dim):
        """返回一个dim维的零向量"""
        return cls([0] * dim)
    
    def norm(self):
        """返回向量的模:向量的长度"""
        return math.sqrt(sum(e**2 for e in self))
    
    def normalize(self):
        """返回向量的单位向量"""
        return Vector(self._values) / self.norm()
    