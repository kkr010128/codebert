def resolve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        n = N//i
        ans += (n*(n+1)*i)//2
    print(ans)


if '__main__' == __name__:
    resolve()
