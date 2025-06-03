import sys
input = sys.stdin.readline

n, s = int(input()), set([])
for i in range(n): s.add(input()[:-1])
print(len(s))