n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

aa = [0]
bb = [0]
for i in range(n):
    aa.append(a[i]+aa[-1])
for i in range(m):
    bb.append(b[i]+bb[-1])
ans = 0
j = m
for i in range(n+1):
    r = k - aa[i]
    while bb[j] > r and j >= 0:
        j -= 1
    if j >= 0:
        ans = max(ans, i+j)
print(ans)