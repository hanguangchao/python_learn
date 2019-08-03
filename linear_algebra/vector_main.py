#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:33:04 2019

@author: han
"""

from vector import Vector

if __name__ == "__main__":
    
    vec = Vector([5,2])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))
    
    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))
    
    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))
    
    
    z = Vector.zero(2)
    print(z)
    print("{} + {} = {}".format(vec, z, vec + z))
    
    zero2 = Vector.zero(2)
    print(zero2)
    print("{} + {} = {}".format(vec, zero2, vec + zero2))

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))
    print("norm({}) = {}".format(zero2, zero2.norm()))

    print("normalize {} is {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())

    print("normalize {} is {}".format(vec2, vec2.normalize()))
    print(vec2.normalize().norm())
    
    
    x = Vector([1, 1, 1])
    y = Vector([2, 4,6])
    print("{} + {} = {}".format(x, y, x + y))
    
    print("{} * {} = {}".format(4, x, 4 * x))
    
    print("norm({}) = {}".format(x, x.norm()))
    
    print("norm({}) = {}".format(y, y.norm()))
    
    print("normalize {} is {}".format(x, x.normalize()))
    print(x.normalize().norm())
    
    
    print("normalize {} is {}".format(y, y.normalize()))
    print(y.normalize().norm())
    
    
    v  = Vector([-0.221, 7.437])
    print("norm({}) = {}".format(v, v.norm()))
    print("normalize {} is {}".format(v, v.normalize()))
    
    v  = Vector([8.813, -1.331, -6.247])
    print("norm({}) = {}".format(v, v.norm()))
    print("normalize {} is {}".format(v, v.normalize()))
    
    x = Vector([1, 1, 1])
    y = Vector([2, 4,6])
    
    print("dot({} . {}) = {}".format(x, y , x.dot(y)))
    