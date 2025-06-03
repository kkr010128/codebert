N,M = map(int,input().split())
H = list(map(int,input().split()))
ab = [map(int, input().split()) for _ in range(M)]
a, b = [list(i) for i  in zip(*ab)]

t = [1]*(N)
#print(N,M,H,t,a,b)
for i in range(M):
    if H[a[i]-1] > H[b[i]-1] :
        t[b[i]-1] = 0
    elif H[a[i]-1] < H[b[i]-1]:
        t[a[i]-1] = 0
    else:
        t[a[i]-1]=0
        t[b[i]-1]=0

ans = 0
for i in t:
    if i == 1:
        ans += 1

print(ans)