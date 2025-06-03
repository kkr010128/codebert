import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    P = [0] * M
    S = [""] * M
    for i in range(M):
        PS = input().split()
        P[i], S[i] = int(PS[0]), PS[1]

    AC = [False] * (N + 1)
    WA = [0] * (N + 1)
    n_AC = 0
    n_WA = 0
    for p, s in zip(P, S):
        if AC[p]:
            continue
        if s == "AC":
            n_AC += 1
            AC[p] = True
            n_WA += WA[p]
        else:
            WA[p] += 1

    print(n_AC, n_WA)


if __name__ == "__main__":
    main()
