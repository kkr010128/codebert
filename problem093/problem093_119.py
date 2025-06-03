N, K = map(int,input().split())
P = [int(x)-1 for x in input().split()]
C = [int(x) for x in input().split()]

def loop(s):
    value = 0
    done = set()
    while s not in done:
        done.add(s)
        s = P[s]
        value += C[s]
    return len(done), value

def f(s,K):
    ans = -10**18
    total = 0
    done = set()
    while s not in done:
        done.add(s)
        s = P[s]
        total += C[s]
        ans = max(ans,total)
        K -= 1

        if K==0:
            return ans

    lamb, value = loop(s)

    if K > 2*lamb:
        if value > 0:
            K -= lamb
            total += (K//lamb)*value
            ans = max(ans,total)
            K -= (K//lamb)*lamb
            K += lamb
    if value <= 0:
        K = min(K,lamb+5)
        


    while K > 0:
        s = P[s]
        total += C[s]
        ans = max(ans,total)
        K -= 1
    return ans

print(max([f(s,K) for s in range(N)]))