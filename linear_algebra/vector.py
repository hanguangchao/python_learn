#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:24:56 2019

@author: han
"""

class Vector:
    #构造方法，传进来的是一个lst数组
    def __init__(self,lst):
        self._values=lst

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
    
    