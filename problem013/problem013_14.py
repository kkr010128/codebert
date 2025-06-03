N=int(input())
R=[int(input()) for x in range(N)]
maxv=-10**9
minv=R[0]
for r in R[1:]:
    maxv = max(r-minv,maxv)
    minv = min(r,minv)
print(maxv)