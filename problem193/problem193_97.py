import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    H, W, K = [int(x) for x in input().split()]
    S = [list(input().strip()) for _ in range(H)]

    ans = float("inf")

    for n in range(2 ** (H - 1)):
        tmp = 0
        wn = [0] * 10

        for i in range(H):
            if n >> i & 1:
                tmp += 1

        for i in range(W):
            f = False
            ni = 0
            for j in range(H):
                if wn[ni] + int(S[j][i]) > K:
                    tmp += 1
                    f = True
                    break
                else:
                    wn[ni] += int(S[j][i])
                if n >> j & 1:
                    ni += 1
            if f:
                if i == 0:
                    tmp = float("inf")
                for j in range(H):
                    wn[j] = 0
                ni = 0
                for j in range(H):
                    wn[ni] += int(S[j][i])
                    if wn[ni] > K:
                        tmp = float("inf")
                    if n >> j & 1:
                        ni += 1

        ans = min(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
