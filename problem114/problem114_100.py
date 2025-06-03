D = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for k in range(D)]
t = [int(input()) for k in range(D)]


ret = 0
last = [0]*26
for k in range(D):
    last[t[k]-1] = k+1
    ret += s[k][t[k]-1]
    for i in range(26):
        ret -= c[i]*(k+1-last[i])
    print(ret)
