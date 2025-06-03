#!/usr/bin/env python
#coding: UTF-8
import sys
import math

i= sys.stdin.readline()

a,b,c = map(int,i.split())

d = math.cos(math.radians(c))
c = math.sin(math.radians(c))

S = 0.5*a*b*c
L = math.sqrt(a**2+b**2-2*a*b*d)+a+b
h = S*2/a

print S,L,h