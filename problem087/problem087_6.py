from sys import stdin
import math
inp = lambda : stdin.readline().strip()

a = list(inp())
a2 = [int(x) for x in a]
if sum(a2) % 9 == 0:
	print("Yes")
else:
	print("No")