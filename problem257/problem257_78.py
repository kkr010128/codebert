def resolve():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 1
    ans = 0
    for i in range(N):
        if a[i] == cnt:
            cnt += 1
        else:
            ans += 1
    if ans == N:
        print(-1)
        return
    print(ans)

    return
resolve()