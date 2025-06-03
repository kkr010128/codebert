# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 16:58:45 2015

@author: hirose
"""

#Branch on Condition - Circle in a Rectangle

n = map(int, raw_input().split())

W = n[0]
H = n[1]
x = n[2]
y = n[3]
r = n[4]

if(x>=r and y>=r and x<=W-r and y<=H-r):
    print "Yes"
else:
    print "No"