N = int(input())
X = list(map(int, input().split()))
ans = 50 ** 2 * 100
for P in range(1,101):
    sum = 0
    for i in range(N):
        sum += (X[i] - P) ** 2
    if sum < ans:
        ans = sum
print(ans)
