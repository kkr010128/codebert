D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]

last_di = [0] * 26

v = 0
for d in range(D):
    i = t[d]
    v += s[d][i - 1]

    last_di[i - 1] = d + 1

    S = 0
    for j in range(len(c)):
        S += c[j] * (d + 1 - last_di[j])

    v -= S
    print(v)