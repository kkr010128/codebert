n, m = map(int, input().split())
a = list(map(int, input().split()))

x = n - sum(a)
print(x) if x >= 0 else print(-1)