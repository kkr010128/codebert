n, k = map(int, input().split())
W = [int(input()) for i in range(n)]

left = max(W)-1; right = sum(W)
while left+1 < right:
    mid = (left + right) // 2
    cnt = 1; cur = 0
    for w in W:
        if mid < cur + w:
            cur = w
            cnt += 1
        else:
            cur += w
    if cnt <= k:
        right = mid
    else:
        left = mid
print(right)