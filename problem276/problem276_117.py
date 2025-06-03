n = int(input())
A = list(map(int, input().split()))
x = sum(A)-A[0]
y = A[0]
ans = abs(x-y)
for a in A[1:]:
    y += a
    x -= a
    ans = min(ans, abs(x-y))
print(ans)