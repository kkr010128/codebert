import numpy as np
n, k = map(int, input().split())
aa = list(map(np.int64, input().split()))
aa = np.array(aa)

def mul(dd):
    mod = 10**9+7
    ret = 1
    for d in dd:
        ret = (ret*d)%mod
    return ret

def sol(aa, n, k):
    mod = 10**9+7
    aap = aa[aa>0]
    aam = aa[aa<0]
    if n == k:
        return mul(aa)
    if len(aap) + 2*(len(aam)//2) < k:
        return 0

    # マイナスのみ
    if len(aam) == n:
        aam.sort()
        if k%2==1:
            return mul(aam[-k:])
        else:
            return mul(aam[:k])

    aap = aa[aa>=0]
    aap.sort()
    aap = aap[::-1]
    aam.sort()

    ret=1
    if k%2 >0:
        k = k-1
        ret *= aap[0]
        aap = aap[1:]

    aap2 = [aap[2*i]*aap[2*i+1] for i in range(len(aap)//2)]
    aam2 = [aam[2*i]*aam[2*i+1] for i in range(len(aam)//2)]
    aap2.extend(aam2)
    aap2.sort(reverse=True)
    aap2 = [i%mod for i in aap2]
    return (ret*mul(aap2[:k//2]))%mod
print(sol(aa, n, k))

