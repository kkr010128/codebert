D = int(input())
Cs = list(map(int,input().split()))
Ss = [list(map(int,input().split())) for i in range(D)]
ts = []
for i in range(D):
    ts.append(int(input()))

last = [0]*26
satisfy = 0

for day,t in enumerate(ts):
    day += 1
    last[t-1] = day
    satisfy += Ss[day-1][t-1]
    for i in range(26):
        satisfy -= Cs[i]*(day-last[i])
    print(satisfy)