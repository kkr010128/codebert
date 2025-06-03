n, k = map(int, input().split())
A = [*map(int, input().split())]
for i in range(k):
    B = [0]*n
    for j in range(n):
        l = max(0, j-A[j])
        r = j + A[j] + 1
        B[l] += 1
        if r <= n-1: B[r] -= 1
    is_same = True
    for j in range(n-1):
        B[j+1] = B[j+1] + B[j]
        if B[j+1] != n: is_same = False
    if is_same: break
    A = B
print(*B,sep=' ')
