#!/usr/bin/env python3

import sys

def cube(x):
	if not isinstance(x,int):
		x = int(x)
	return x*x*x

if __name__ == '__main__':
	i = sys.stdin.readline()
	print('{}'.format( cube( int(i) ) ))