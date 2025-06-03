N, M = map(int,input().split())

ans = [["",0] for i in range(N)]
for i in range(M):
    p,S = map(str,input().split())
    p = int(p)-1
    if ans[p][0] != "AC":
        if S == "AC":
            ans[p][0] = "AC"
        elif S == "WA":
            ans[p][1] += 1

AC = 0
WA = 0
for i in ans:
    if i[0] == "AC":
        AC += 1
        WA += i[1]

print(AC,WA)