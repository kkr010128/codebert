def penalty(day, last, c):
    val = 0
    for i in range(26):
        val += c[i] * (day - last[i])
    return val

d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input()) for _ in range(d)]

last = [-1]*26
ans = [0]*(d+1)

for day in range(d):
    ans[day+1] = ans[day] + s[day][t[day]-1]
    last[t[day]-1] = day
    ans[day+1] -= penalty(day, last, c)

for v in ans[1:]:
    print(v)