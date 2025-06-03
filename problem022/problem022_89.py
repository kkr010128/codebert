import sys

n = int(sys.stdin.readline().strip())
S = map(int, sys.stdin.readline().strip().split(" "))

n = int(sys.stdin.readline().strip())
T = map(int, sys.stdin.readline().strip().split(" "))

res = []

for t in T:
    res.append(int(S.count(t) != 0))
print sum(res)