n = int(input())
A = list(map(int, input().split()))
l = A[0]
r = sum(A[1:])
x = abs(l-r)
for a in A[1:]:
    l += a
    r -= a
    if x > abs(l-r): x = abs(l-r)
print(x)