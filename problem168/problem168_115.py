r=input().split()
N=int(r[0])
d_pre=input().split()
d=[int(s) for s in d_pre]
ans=N-sum(d)
if ans>=0:
    print(ans)
else:
    print(-1)