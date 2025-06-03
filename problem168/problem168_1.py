n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
for ai in a:
  n -= ai
n = -1 if n < 0 else n
print(n)