# encoding:utf-8
import math as ma
# math.pi
x = float(input())

pi = (x * x) * ma.pi
# Circumference
pi_line = (x + x) * ma.pi

print("{0} {1}".format(pi,pi_line))