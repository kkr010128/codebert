n = int(input())
A = list(map(int, input().split()))

x = 1000
for i in range(n-1):
    if A[i] < A[i+1]:
        q, x = divmod(x, A[i])
        x += q*A[i+1]
print(x)