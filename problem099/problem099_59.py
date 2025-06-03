n, k = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = 10**9+1

while l < r:
    mid = (l+r)//2
    count = 0
    for i in range(n):
        if A[i] > mid:
            count += A[i]//mid

    if count <= k:
        r = mid
    else:
        l = mid+1


print(l)