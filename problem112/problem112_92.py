import numpy as np

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    mod = int(1e9+7)
    p = []
    m = []
    for a in A:
        if a >= 0:
            p.append(a)
        else:
            m.append(a)
    p.sort(reverse=True)
    m.sort(reverse=False)
    ans = 1
    if sum(np.sign(A)) == -N and K%2 == 1:
        A = sorted(A, reverse=True)
        for i in range(K):
            ans = (ans*A[i])%mod
        print(ans)
        return
    if N == K:
        for i in range(K):
            ans = (ans*A[i])%mod
        print(ans)
        return

    m_pair = []
    p_pair = []
    if K%2 == 1:
        ans *= p.pop(0)%mod
    for i in range(0, len(m), 2):
        if i+1 < len(m):
            m_pair.append(m[i]*m[i+1])
        # else:
        #     m_pair.append(m[i])
    for i in range(0, len(p), 2):
        if i+1 < len(p):
            p_pair.append(p[i]*p[i+1])
        else:
            p_pair.append(p[i])
    pairs = m_pair[:]
    pairs.extend(p_pair)
    pairs.sort(reverse=True)
    for i in range(K//2):
        ans = (ans*pairs[i])%mod
    print(ans)

main()
