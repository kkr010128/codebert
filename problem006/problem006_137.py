#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main(): 
	week = int(input())
	base = 100000
	x = base
	for i in range(week):
		x = round(x * 1.05)
		if x % 1000 > 0:
			x = (x // 1000) *1000 +1000
	print(x)
if __name__ == '__main__':
  main()