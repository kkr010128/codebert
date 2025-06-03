N = int(input())
A = list(map(int, input().split()))

m = 1000
k = 0
for i in range(N-1):
    if A[i] > A[i+1]:
        m += k * A[i]
        k = 0
    elif A[i] < A[i+1]:
        m += k * A[i]
        k = m // A[i]
        m -= k * A[i]
    else:
        pass
m += (k * A[-1])
print(m)
