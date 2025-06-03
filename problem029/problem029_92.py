#coding:utf-8

import math

datas = [float(x) for x in input().split()]
p1 = (datas[0], datas[1])
p2 = (datas[2], datas[3])

print(math.sqrt(math.pow(p1[0]-p2[0], 2)+math.pow(p1[1]-p2[1],2)))