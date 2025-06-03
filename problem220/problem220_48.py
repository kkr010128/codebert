import sys
import collections
input = sys.stdin.readline

s, t = map(str,input().split())
a, b = map(int, input().split())
u = input().strip()
if u == s:
	print(a - 1, b)
else:
	print(a, b - 1)