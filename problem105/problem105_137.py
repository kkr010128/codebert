n = int(input())
data = list(map(int, input().split()))

ans = []

for i in range(n):
    if (i % 2 == 0) and (data[i] % 2 == 1):
        ans.append(data[i])

print(len(ans))
