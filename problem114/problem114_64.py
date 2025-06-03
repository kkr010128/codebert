def resolve():
    D = int(input())
    C = [int(x) for x in input().split()]
    S = []
    for i in range(D):
        S.append(list(map(int, input().split())))
    t = [int(input()) for _ in range(D)]
    last_d = []
    score = 0

    for d in range(D):
        score += S[d][t[d] - 1]
        last_d.append(t[d] - 1)
        for i in range(len(C)):
            if i in last_d:
                score -= C[i] * last_d[::-1].index(i)
            else:
                score -= C[i] * (d + 1)
        print(score)


if __name__ == "__main__":
    resolve()