a, b, c, d = map(int, input().split())

i = 0
i1 = 0

while a > 0:
    a -= d
    i += 1

while c > 0:
    c -= b
    i1 += 1

if i >= i1:
    print('Yes')
else:
    print('No')
