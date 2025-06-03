d = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for _ in range(d)]
t = [int(input()) for _ in range(d)]

lastd = [0]*26
point = 0

for j,k in enumerate(t):
    kk = k-1
    point += s[j][kk]
    lastd[kk] = j+1
    for l in range(26):
        point -= c[l]*(j+1-lastd[l])
    print(point)