#!/usr/bin/python3
#coding: utf-8

N = int(input())

p = 10**9 + 7

ret = pow(10, N)
ret -= pow(9, N) 
ret -= pow(9, N)
ret += pow(8, N)

ret %= p

print(ret)