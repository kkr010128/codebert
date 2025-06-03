n,m,q = map(int,input().split())
pairs = []
def makelen(a):
    if len(a) == n:
        pairs.append(a)
    else:
        for i in range(a[-1],m+1):
            makelen(a + [i])
for i in range(m):
    makelen([i+1])
Query = [list(map(int,input().split())) for _ in range(q)]
ans = 0
for pair in pairs:
    tmpans = 0
    for a,b,c,d in Query:
        if pair[b-1] - pair[a-1] == c:
            tmpans += d
    ans = max(tmpans,ans)
print(ans)