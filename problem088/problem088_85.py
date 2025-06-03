n = int(input())
A = list(map(int, input().split()))
m = A[0]
ans = 0
for a in A[1:]:
    m = max(m,a)
    if m > a:
        ans += m-a
print(ans)