n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = max(a)

while r - l > 1:
    cnt = 0
    mid = (r + l) // 2
    for i in range(n):
        d = (a[i] // mid) + (a[i] % mid != 0) - 1
        cnt += d
    if cnt <= k: r = mid
    else: l = mid 

print(r)