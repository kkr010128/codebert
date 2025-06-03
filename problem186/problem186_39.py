K, N = [int(a) for a in input().split()]
A = [int(a) for a in input().split()]

max_diff = 0
dsum = 0
for i in range(len(A)):
    if i < len(A)-1:
        diff = A[i+1] - A[i]
    else:
        diff = K - A[i] + A[0]
    dsum += diff
    if diff > max_diff:
        max_diff = diff

ans = dsum - max_diff
print(ans)