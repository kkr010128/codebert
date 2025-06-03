def main():
    N, K = map(int, input().split())
    *P, = map(int, input().split())

    P.sort()
    print(sum(P[:K]))


if __name__ == '__main__':
    main()
