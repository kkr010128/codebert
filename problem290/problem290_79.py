N,K=list(map(int,input().split()))
A=sorted(list(map(int,input().split())))
F=sorted(list(map(int,input().split())),reverse=True)

ok=10**12
ng=0

while abs(ok-ng)>0:
    center=(ok+ng)//2
    cnt=0

    for i in range(N):
        ap=center//F[i]
        cnt+=max(0,A[i]-ap)
        if K<cnt:
            ng=center+1
            break
    else:
        ok=center

print(ok)