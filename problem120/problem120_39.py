n, k = map(int, input().split())
p = [int(x) for x in input().split()]
p.sort()

ans = sum(p[0:k])
print(ans)
