n = int(input())
p = list(map(int, input().split()))
ret = 1
minp = p[0]
for i in range(1, n):
    if p[i] <= minp:
        ret += 1
    minp = min(minp, p[i])
print(ret)
