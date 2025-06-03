
def resolve():
    N = int(input())
    ans = 0
    counts = [1 for _ in range(N+1)]
    for i in range(2, N+1):
        j = 1
        while i*j <= N:
            counts[i*j] += 1
            j += 1

    for i in range(1, N+1):
        ans += i*counts[i]
    print(ans)


if '__main__' == __name__:
    resolve()