D = int(input())
c = [0]+list(map(int, input().split()))
s = [[0]]+[[0]+list(map(int, input().split())) for _ in range(D)]
t = [0]+[int(input()) for _ in range(D)]
ans = 0
last = [0]*(27)
for d in range(1,D+1):
    ans += s[d][t[d]]
    last[t[d]] = d
    for i in range(1,27):
        ans -= c[i] * (d-last[i])
    print(ans)