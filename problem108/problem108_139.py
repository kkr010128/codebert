#!/usr/bin/python3
n = int(input())
if(n%1000==0):
	print("0")
else:
	ans = n%1000
	print(1000-ans)