N,M = map(int,input().split())
H = list(map(int,input().split()))
L = [ list(map(int,input().split())) for i in range(M) ]

d = { k+1:True for k in range(N) }

for l in L :
    if H[l[0]-1] <= H[l[1]-1] :
        d[l[0]] = False
    if H[l[0]-1] >= H[l[1]-1] :
        d[l[1]] = False 
    
ans = 0
for v in d.values() :
    if v :
        ans += 1

print(ans)