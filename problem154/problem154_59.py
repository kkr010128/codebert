def Qb():
    n, k = map(int, input().split())
    ans = set()
    for v in range(k):
        d = int(input())
        ns = [int(v) for v in input().split()]
        for N in ns:
            ans.add(N)
    print(n - len(ans))


if __name__ == '__main__':
    Qb()
