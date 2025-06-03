def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    from itertools import accumulate
    acc = [a for a in accumulate([0] + A)]
    ans = acc[-1]
    for i in range(1, N+1):
        a = acc[i]
        b = acc[N] - acc[i]
        v = abs(a-b)
        ans = min(ans, v)
    print(ans)


if __name__ == '__main__':
    main()
