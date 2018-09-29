#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:58:03 2018

@author: michaelmiranda
"""

class Rect(object):
    def __init__(self, height=10, width=5):
        self.height = height
        self.width = width
        
    def area(self):
        return (self.height * self.width)
    
c1 = Rect(7, 7)
c2 = Rect(14, 3)
print(c1.area(), c2.area())
#print(type(c1))
c1.height = 20
#print(c1.area())

if __name__=='__main__':
    print("I'm UTSA")
else:
    print("I'm not UTSA")

import numpy as np
try:
    y = 17 / 0
except:
    y = np.infinity
    print("You know that is not going to work")
print(y)