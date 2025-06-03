import sys
input = sys.stdin.readline

def factors(x: int) -> list:
    s, xx = [], x
    for i in range(2, int(x ** 0.5 + 1)):
        if xx % i == 0:
            c = 0
            while xx % i == 0: c += 1; xx //= i
            s.append((i, c))
    if xx != 1: s.append((xx, 1))
    if s == []: s.append((x, 1))
    return s

n, res = int(input()), 0
f = factors(n)
pre = [1, 3, 6, 10, 15, 21, 28, 36, 43]
flag = False
if len(f) == 1 and f[0][0] == 1: print(0); flag = True
if not flag:
    for fact in f:
        for i in range(len(pre)):
            if pre[i] > fact[1]: res += i; break
    print(res)