D = int(input())
c = list(map(int, input().split()))
s_tbl = [list(map(int, input().split())) for _ in range(D)]
ans = 0
last = [0] * 26

for d in range(1, D+1):
    t = int(input()) - 1
    c_sum = 0
    for i in range(26):
        c_sum = c_sum + c[i] * (d-last[i])
    ans = ans + s_tbl[d-1][t] + (-c_sum) + c[t] * (d-last[t])
    last[t] = d
    print(ans)