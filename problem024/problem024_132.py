def check(P):
    global w, k
    t=1
    wt=0
    for wi in w:
        if wt+wi>P:
            wt=wi
            t+=1
        else:
            wt+=wi
        if t>k:
            return False
    return True

def search(l, r):
    if r-l==1:
        return r
    else:
        m=(l+r)//2
        if not check(m):
            return search(m,r)
        else:
            return search(l,m)

n,k=map(int,input().split())
w=[]
for i in range(n):
    w.append(int(input()))
S=sum(w);M=max(w)
#print(S,M)
P0=M-1
#print(P0)

print(search(M-1,S))
