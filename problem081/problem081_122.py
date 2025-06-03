from sys import stdin
inp = lambda : stdin.readline().strip()

d, t, s = [int(x) for x in inp().split()]
if d / s <= t:
    print('Yes')
else:
    print('No')