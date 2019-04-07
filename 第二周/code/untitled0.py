# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 03:00:31 2019

@author: js
"""
import time
a = []
t0 = time.clock()
for i in range(1,20000000):
    a.append(i)
print(time.clock() - t0, "seconds process time")
t0 = time.clock()
b = [i for i in range(1,20000000)]
print(time.clock() - t0, "seconds process time")