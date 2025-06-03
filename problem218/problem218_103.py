import sys

input = sys.stdin.readline
d = {}
for _ in range(int(input())):
    s = input().replace("\n", "")
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

x = max(d.values())
l = sorted(s for (s, i) in d.items() if i == x)
print(*l, sep="\n")