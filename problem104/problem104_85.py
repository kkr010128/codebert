def count(n, d):
    return n // d


def main():
    L, R, d = map(int, input().split())
    ans = count(R, d) - count(L - 1, d)
    print(ans)


if __name__ == '__main__':
    main()
