n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [0 for i in range(n+1)]
b = [0 for j in range(m+1)]
for i in range(n):
    a[i+1] = a[i]+A[i]
for j in range(m):
    b[j+1] = b[j]+B[j]

j = m
res = 0
for i in range(n+1):
    if a[i] > k:
        break
    while k - a[i] < b[j]:
        j -= 1
    res = max(res, i+j)

print(res)