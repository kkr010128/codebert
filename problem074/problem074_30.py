def main():
    N, K = map(int,input().split())

    mod = 998244353

    S = []
    for _ in range (K):
        S.append(list(map(int,input().split())))

    S.sort()
    #print(S)

    ans = [0]*N
    acc = [0]*N
    ans[0] = 1
    acc[0] = 1

    for i in range (1,N):
        for l,r in S:

            if i-l < 0:
                break
            else:
                ans[i] += acc[i-l]
            if i-r -1 < 0:
                break
            else:
                ans[i] -= acc[i-r-1]

        ans[i] %= mod
        acc[i] = (acc[i-1]+ans[i])%mod


    print(ans[N-1])


main()
