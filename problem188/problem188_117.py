def main():
    X, Y, A, B, C = map(int, input().split())
    *P, = map(int, input().split())
    *Q, = map(int, input().split())
    *R, = map(int, input().split())

    P.sort(reverse=True)
    Q.sort(reverse=True)

    ans = sum(sorted(P[:X] + Q[:Y] + R, reverse=True)[:X + Y])
    print(ans)


if __name__ == '__main__':
    main()
