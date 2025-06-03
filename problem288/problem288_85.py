N = int(input())
ans = N - 1
for i in range(2, int((N ** 0.5) + 1)):
    if N % i == 0:
        j = N // i
        m = i + j - 2
        ans = min(ans, m)
print(ans)
