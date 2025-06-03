N, M = map(int, input().split())
Q = [list(map(str, input().split())) for _ in range(M)]

ans = [0] * N
AC = 0
WA = 0

for P in Q:
    p = int(P[0])
    S = P[1]
    if ans[p - 1] == "END":
        continue
    if S == "WA":
        ans[p - 1] += 1
    if S == "AC":
        WA += ans[p - 1]
        AC += 1
        ans[p - 1] = "END"


print(AC, WA)
