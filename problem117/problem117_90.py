n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_A = [0 for _ in range(n+1)] # sum_A[i]:=上からi冊の本を読むときにかかる時間
for i in range(1, n+1):
    sum_A[i] = sum_A[i-1] + A[i-1]
sum_B = [0 for _ in range(m+1)] # sum_B[i]:=上からj冊の本を読むときにかかる時間
for j in range(1, m+1):
    sum_B[j] = sum_B[j-1] + B[j-1]

ans = 0
i = 0
j = m
while i <= n and sum_A[i] <= k:
    while sum_A[i] + sum_B[j] > k:
        j -= 1
    ans = max(ans, i + j)
    i += 1
print(ans)