n = int(input())
p = list(map(int, input().split()))

cnt = 0
p_min = 2*10**5+1
for i in range(n):
    if p_min >= p[i]:
        cnt += 1
    p_min = min(p_min, p[i])

print(cnt)