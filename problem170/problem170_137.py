def resolve():
    N, K = list(map(int, input().split()))
    ans = 0
    mini = sum(range(K))
    maxi = sum(range(N, N-K, -1))
    for i in range(K, N+2):
        ans += maxi - mini + 1
        ans %= 10**9+7
        mini += i
        maxi += N - i
    print(ans)        


if '__main__' == __name__:
    resolve()
