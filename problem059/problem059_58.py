r,_=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(r)]
[s.append(sum(s))or print(*s)for s in a]
print(*[sum(c)for c in zip(*a)])