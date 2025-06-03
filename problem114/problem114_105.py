D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(D)]

t = [int(input()) for i in range(D)]

last = [0]*26
S = 0
for d in range(1, D+1):
    # last更新
    for j in range(26):
        if j == t[d-1]-1:
            last[j] = d

    # plus部分
    S += s[d-1][t[d-1]-1]

    # minus部分
    m = 0
    for j in range(26):
        m += c[j] * (d-last[j])
    
    S -= m
    
    print(S)