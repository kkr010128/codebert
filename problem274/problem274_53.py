def main():
    N, M = map(int, input().split())
    *G, = map(int, input())

    ans = []
    cur = N
    ecur = cur - 1
    while cur > 0:
        ncur = cur
        while (cur - ecur) <= M and ecur >= 0:
            if G[ecur] == 0:
                ncur = ecur
            ecur -= 1

        if ncur == cur:
            print(-1)
            return

        ans.append(cur - ncur)
        cur = ncur

    ans.reverse()

    print(*ans)


if __name__ == '__main__':
    main()
