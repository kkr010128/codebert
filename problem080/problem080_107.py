N=int(input())
DMY=10**9

mmax=None
mmin=None
dmax=None
dmin=None
for i in range(N):
    x,y = map(int, input().split())
    if not mmax:
        mmax=(x,y,x+y)
        mmin=(x,y,x+y)
        dmax=(x,y,x+DMY-y)
        dmin=(x,y,x+DMY-y)
        continue
    if x+y > mmax[2]:
        mmax=(x,y,x+y)
    elif x+y < mmin[2]:
        mmin=(x,y,x+y)
    if x+DMY-y > dmax[2]:
        dmax=(x,y,x+DMY-y)
    elif x+DMY-y < dmin[2]:
        dmin=(x,y,x+DMY-y)

print(max(mmax[2]-mmin[2],dmax[2]-dmin[2]))
