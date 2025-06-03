n, m, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

total = 0
count = 0
flag = n-1
for i in range(n):
    total += a[i]
    if total > k:
        total -= a[i]
        flag = i-1
        break
    count += 1
ans = count
for i in range(m):
    if b[i] > k:
        break
    total += b[i]
    count += 1
    while total > k:
        if flag == -1:
            break
        else:
            total -= a[flag]
            flag -= 1
            count -= 1
    if total > k: 
        break
    ans = max(ans, count)

print(ans)