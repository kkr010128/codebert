n, m = map(int, input().split())

a = list(map(int, input().split()))
sum = 0
for i in range(len(a)):
    sum += a[i]

if sum <= n:
    print(n - sum)
else:
    print(-1)