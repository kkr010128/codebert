#!/usr/bin/env python
#coding: UTF-8
import sys

a = sys.stdin.readlines()
b = []

for i in a:
		for j in i:
			b.append(j.lower())
for i in range(97, 97+26):
	print chr(i)+" : "+str(b.count(chr(i)))