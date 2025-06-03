# AOJ ALDS1_4_C Dictionary
# Python3 2018.7.3 bal4u

import sys
from sys import stdin
input = stdin.readline

dic = {}
n = int(input())
for i in range(n):
	s = input()
	if s[0] == 'i': dic[s[7:]] = 1
	else: print("yes" if s[5:] in dic else "no")
