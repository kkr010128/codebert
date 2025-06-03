def resolve():
    N = int(input())
    pow = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                ans += pow[i]*pow[j]
    print(ans//2)
resolve()