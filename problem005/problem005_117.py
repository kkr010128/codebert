#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	while True:		
		try:
			a, b = [int(x) for x in input().split(" ")]
		except:
			return
		else:
			print(gcd(a, b),lcm(a, b))
def lcm(a, b):
	return (a * b) // gcd(a,b)
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a	
			
if __name__ == '__main__':
  main()