n, k = map(int, input().split())
p = list(map(int, input().split()))

pp = sorted(p)
ans = sum(pp[:k])
print(ans)
