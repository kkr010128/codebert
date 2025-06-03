def main():

    N = int(input())

    d = dict()
    for i in range(1, N+1):
        u = int(str(i)[0])
        v = int(str(i)[-1])
        d[(u, v)] = d.get((u, v), 0) + 1

    ans = 0
    for u, v in d:
        if (v, u) in d:
            ans += d[(u, v)] * d[(v, u)]
    return ans


if __name__ == '__main__':
    print(main())
