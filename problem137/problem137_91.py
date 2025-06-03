n = int(input())
aa = []
bb = []

for _ in range(n):
    a, b = map(int, input().split())
    aa.append(a)
    bb.append(b)

aa.sort()
bb.sort()

if n % 2 == 1:
    ac = aa[n // 2]
    bc = bb[n // 2]
    print(abs(ac - bc) + 1)

else:
    ac1 = aa[n // 2 - 1]
    bc1 = bb[n // 2 - 1]
    ac2 = aa[n // 2]
    bc2 = bb[n // 2]
    print((bc2 + bc1) - (ac2 + ac1) + 1)
