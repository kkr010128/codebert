n, k, s = map(int, input().split())
a = [0 for i in range(n)]
for i in range(k):
    a[i] = s
if s == 10**9:
    for j in range(n-k):
        a[k+j] = 10**9-1
else:
    for j in range(n-k):
        a[k+j] = s+1

print(*a)
