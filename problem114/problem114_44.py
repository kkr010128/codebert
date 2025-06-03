D = int(input())
c = list(map(int, input().split()))
last = [0] * 26
S = []
for d in range(1, D+1):
    sd = list(map(int, input().split()))
    S += [sd]
score = 0
for d in range(1, D+1):
    td = int(input()) - 1

    cumsump = 0
    for i in range(26):
        if td != i:
            tmp = -c[i] * (d - last[i])
            cumsump += tmp
    last[td] = d
    score += S[d-1][td]+cumsump
    
    print(score)