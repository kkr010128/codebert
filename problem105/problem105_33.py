import sys
n = int(sys.stdin.readline().rstrip("\n"))
a = [int(s) for s in sys.stdin.readline().rstrip("\n").split()]
i = 0
s = 0
while i < n:
    if a[i] % 2 == 1:
        s += 1
    i += 2
print(s)