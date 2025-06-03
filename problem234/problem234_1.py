n = int(input())
tbl = [[0]*10 for _ in [0]*10]
k = 10
for i in range(1, n+1):
    if i // k: k *= 10
    l = i*10//k
    r = i%10
    tbl[l][r] += 1
    
ans = 0
for l, _t in enumerate(tbl):
    for r, t in enumerate(_t):
        if l == r:
            ans += t*t
        else:
            ans += t*tbl[r][l]
print(ans)