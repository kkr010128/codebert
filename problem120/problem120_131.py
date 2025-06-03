n, k = map(int, input().split())
p = sorted(map(int, input().split()))
i = 0
for j in range(k):
    i = i + p[j]
print(i)