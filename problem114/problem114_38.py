d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input()) for _ in range(d)]

last = [[0] * d for _ in range(26)]  # 26xd

ans = 0
for i in range(d):
    type = t[i]  # 1~26
    contest = c[type-1]
    satisfy = s[i][type-1]
    ans += satisfy
    last[type-1][i:] = [i+1] * (d-i)

    for j in range(26):
        ans -= c[j] * ((i+1)-last[j][i])
    print(ans)