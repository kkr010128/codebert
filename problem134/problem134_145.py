def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    th = 10**18
    if 0 in A:
        print(0)
        return
    for a in A:
        ans *= a
        if ans > th:
            print(-1)
            return 
    print(ans if ans <= th else -1)

if '__main__' == __name__:
    resolve()