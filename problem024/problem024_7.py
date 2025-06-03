n,k = map(int,input().split())
w = [int(input()) for _ in range(n)]
left = max(w)-1
right = sum(w)

while (right - left) > 1:
    mid = (left + right)//2
    count = 1
    c = 0
    for s in w:
        if mid < c + s:
            c = s
            count += 1
        else:
            c += s
    if count <= k:
        right = mid
    else:
        left = mid
print(right)
