from decimal import Decimal

n,m = map(int, input().split())
A = list(map(int, input().split()))
line = Decimal(sum(A) / (4 * m))
cnt = 0
for a in A:
    if a >= line:
        cnt += 1
    if cnt >= m:
        print('Yes')
        break
else:
    print('No')