import sys

n = sys.stdin.readlines()
for i in n:
    a = [int(x) for x in i.split()]
    if a[0] == 0 and a[1] == 0:
        break
    print(*sorted(a))