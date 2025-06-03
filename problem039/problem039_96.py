#---------------------------------------------------------------
# coding: utf-8
# Python 3+
import sys

#file = open("test.txt")
file = sys.stdin

a, b, c = map(int, file.readline().split())

if a < b < c :
    print("Yes")
else :
    print("No")