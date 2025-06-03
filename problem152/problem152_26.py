#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

n = inn()
ls = []
rs = []
z = 0
for i in range(n):
    ss = ins()
    l = r = 0
    for c in ss:
        if c=='(':
             l += 1
        else:
            if l>0:
                l -= 1
            else:
                r += 1
    rr = r
    l = r = 0
    for j in range(len(ss)-1,-1,-1):
        c = ss[j]
        if c==')':
             r += 1
        else:
            if r>0:
                r -= 1
            else:
                l += 1
    r = rr
    if l>r:
        ls.append((r,l-r))
    elif l<r:
        rs.append((l,r-l))
    else:
        z = max(z,r)
ls.sort()
rs.sort()
#ddprint(ls)
#ddprint(rs)
#ddprint(z)
l = r = 0
for rr,ll in ls:
    if l<rr:
        print('No')
        exit()
    l = l+ll
for ll,rr in rs:
    if r<ll:
        print('No')
        exit()
    r = r+rr
print('Yes' if l==r>=z else 'No')
