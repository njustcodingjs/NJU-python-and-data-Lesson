# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:52:58 2019

@author: js
"""
a = input("please input a number:")
number = eval(a)
if 100>=number>=90:
    print("A")
elif 89>=number>=70:
    print("B")
elif 79>=number>=60:
    print("C")
elif 59>=number>=0:
    print("D")
else:
    print("Fail")