n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

aa = [0]
bb = [0]
for i in range(n):
    aa.append(aa[-1]+a[i])
for i in range(m):
    bb.append(bb[-1]+b[i])
c = m
ans = 0
for i in range(n+1):
    u = k - aa[i]
    for j in range(c, -1, -1):
        if bb[j] <= u:
            ans = max(ans, i+j)
            c = j
            break
print(ans)