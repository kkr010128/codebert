k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(a[0] + k)
dist = [a[i + 1] - a[i] for i in range(n)]
print(sum(dist) - max(dist))

