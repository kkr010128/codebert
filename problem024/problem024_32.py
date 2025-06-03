n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

left = 0
right = 100000*10000

while (right - left > 1):
    mid = (left + right)//2
    s = 0
    j = 1
    for i in range(n):
        if mid < w[i]:
            j = 100000
            break
        s += w[i]
        if s > mid:
            j += 1
            s = w[i]
    if j > k:
        left = mid
    else:
        right = mid
        
print(right)
