import math
n,k = map(int,input().split())
A = list(map(int,input().split()))

low = 1
high = max(A)

while low != high:
    mid = (low + high)// 2
    cnt = 0
    for i in A:
        cnt += math.ceil(i/mid) - 1
    if cnt > k :
        low = mid + 1
    else:
        high = mid

print(low)