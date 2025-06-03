from math import ceil

n, m = (int(x) for x in input().split())
if n % 2 == 1:
    for i in range(1, m + 1):
        print(i, n - i)
else:
    k = (n - 2) // 2
    l = ceil(k / 2)
    ANS = []
    for i in range(1, l+1):
        ANS.append((i, n - i + 1))
    for i in range(l+2, k+2):
        ANS.append((i, n - i + 2))
    for a, b in ANS[:m]:
        print(a, b)