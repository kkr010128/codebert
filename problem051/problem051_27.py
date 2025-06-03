#!/usr/bin/env python
#coding: UTF-8

import sys

while True:
	hight,width = map (int,raw_input().split())
	if hight+width == 0:
		break
	else:
		for h in range(hight):
			if h%2 == 0:
				for w in range(width):
					if w%2 == 0:
						sys.stdout.write("#")
					else:
						sys.stdout.write(".")
				print ""
			else:
				for w in range(width):
					if w%2 == 0:
						sys.stdout.write(".")
					else:
						sys.stdout.write("#")
				print ""
		print ""