n = int(input())
list_A = list(map(int, input().split()))
ans = 0
m = list_A[0]
for i in range(n):
    if m > list_A[i]:
        ans += m - list_A[i]
    m = max(m, list_A[i])

print(ans)