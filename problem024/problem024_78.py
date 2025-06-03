n,k = map(int,input().split())
a = [int(input()) for s in range(n)]
pmax = sum(a)
pmin = pmax//k-1

def check(ptest):
    tk = 1
    p = 0
    global a,k,n
    i = 0
    while i < n:
        p += a[i]
        if p <= ptest:
            i += 1
        else:
            tk += 1
            p = 0
        if tk > k:
            return False
    return True

while (pmax-pmin) > 1:
    pmid = (pmax+pmin)//2
    if check(pmid):
        pmax = pmid
    else:
        pmin = pmid
print(pmax)


