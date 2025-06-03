n, k = map(int, input().split(" "))
p = list(map(int, input().split(" ")))

p.sort()
ans = sum(p[0:k])
print(ans)