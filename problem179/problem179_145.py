n, m = map(int,input().split())
a = list(map(int,input().split()))
h = sum(a)/(4*m)
ans = 0

for i in range(n):
    if a[i] < h:
        continue
    else:
        ans += 1

if ans < m:
    print('No')
else:
    print('Yes')
