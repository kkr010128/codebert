INF = 10**8


def main():
    N, M, X = (int(i) for i in input().split())
    T = [[int(i) for i in input().split()] for j in range(N)]

    answer = INF
    for bit in range(1, 1 << N):
        intelligibility = [0]*M
        current_money = 0
        for i in range(N):
            if bit & 1 << i:
                current_money += T[i][0]
                for j, a in enumerate(T[i][1:]):
                    intelligibility[j] += a
        if all(X <= intelligence for intelligence in intelligibility):
            answer = min(answer, current_money)
    print(answer if answer != INF else -1)


if __name__ == '__main__':
    main()
