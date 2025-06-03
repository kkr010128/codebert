import numpy as np
n = int(input())

st = [input().split() for _ in range(n)]
x = input()
s, t = zip(*st)
i = s.index(x)
print(sum(map(int, t[i+1:])))
