n = list(map(int, input().split(' ')))
m = list(map(int, input().split(' ')))
if n[0] >=  sum(m):
    print(n[0] - sum(m))
else:
    print(-1)
