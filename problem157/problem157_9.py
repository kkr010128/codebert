
N = int(input())
A = list(map(int,input().split()))
d = {}
ans = 0
for i in range(N):
    sa = i-A[i]
    if sa in d:
        ans += d[sa]
    wa = i+A[i]
    if wa in d:
        d[wa] += 1
    else:
        d[wa] = 1
print(ans)
