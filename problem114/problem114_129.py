D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
T = [int(input()) for _ in range(D)]

ans = []
val = 0
sch = [0]*26
for d in range(D):
    day = d+1
    t = T[d]-1
    sch[t] = day

    down = 0
    for i in range(26):
        down += C[i]*(day - sch[i])

    val = val + S[d][t] - down
    ans.append(val)

print(*ans, sep="\n")