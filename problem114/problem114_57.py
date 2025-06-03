def down(d, last, c):
    result = 0
    for i in range(26):
        result += c[i] * (d - last[i])
    return result


def main():
    D = int(input())
    C = [int(c) for c in input().split()]

    S = [0] * D

    for d in range(D):
        S[d] = [int(s) for s in input().split()]

    last = [0] * 26

    score = 0
    scores = [0] * D
    for d in range(D):
        t = int(input()) - 1

        score += S[d][t]
        last[t] = d + 1

        score -= down(d + 1, last, C)
        scores[d] = score

    for score in scores:
        print(score)


if __name__ == "__main__":
    main()
