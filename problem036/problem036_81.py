#coding:utf-8
import sys

ab=sys.stdin.readline()
rect=ab.split( ' ' )
for i in range(2):
	rect[i]=int( rect[i])
print( "{} {}".format( rect[0]*rect[1], rect[0]*2+rect[1]*2) )