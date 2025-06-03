#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	a, b, m =[int(i) for i in input().split(" ")]
	res = 0
	for i in range(a, b + 1):
		if m % i == 0:
			res += 1
			
	print(res)
if __name__ == '__main__':
  main()