n, k = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A = sorted(A)
Minus_A = [-x for x in A]
F = sorted(F, reverse=True)

high = 10**12
low = 0
while high - low > 1:
    mid = low + (high-low)//2
    count = 0

    for i in range(n):
        now = mid // F[i]
        count += max(A[i] - now, 0)
    
    # print('-'*30)
    # print(mid)
    # print(count)
    if count > k:
        low = mid
    else:
        high = mid
    
ans = high

if sum(A) <= k:
    ans = 0

print(ans)
