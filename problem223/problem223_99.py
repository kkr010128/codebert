def resolve():
    N, K = list(map(int, input().split()))
    P = list(map(int, input().split()))
    total = 0
    ans = 0
    for i in range(N):
        if i < K:
            total += (P[i]+1)/2
            if i == K-1:
                ans = max(ans, total)
        else:
            total -= (P[i-K]+1)/2
            total += (P[i]+1)/2
            ans = max(ans, total)
    print(ans)
        

if '__main__' == __name__:
    resolve()
