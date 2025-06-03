import math
n, m = [int(i) for i in input().split()]
t = 0
tt = 0
def com(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
if n > 1:
    t = com(n,2)
if m > 1:
    tt = com(m,2)

print(t+tt)