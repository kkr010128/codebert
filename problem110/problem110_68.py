h,w,k=map(int,input().split())
ans = 0
def get(sta):
    ret = set()
    for i in range(6):
        if sta & 1:
            ret.add(i)
        sta //= 2
    return ret
grd=[input() for i in range(h)]
for i in range(2**h):
    hs=get(i)
    for j in range(2**w):
        ws=get(j)
        chk = 0
        for a in range(h):
            for b in range(w):
                if a in hs or b in ws or grd[a][b]==".":continue
                chk += 1
        if chk == k:
            ans += 1
print(ans)