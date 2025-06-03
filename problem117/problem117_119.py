n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sums, b_sums = [0], [0]
for i in range(n):
    a_sums.append(a_sums[i] + a[i])
for i in range(m):
    b_sums.append(b_sums[i] + b[i])

ans = 0
j = m
for i in range(n + 1):
    if a_sums[i] > k:
        break
    while a_sums[i] + b_sums[j] > k:
        j -= 1
    ans = max(ans, i + j)

print(ans)