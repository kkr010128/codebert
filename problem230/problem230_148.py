import sys

read = sys.stdin.buffer.read


def main():
    N, D, A, *XH = map(int, read().split())
    monster = [0] * N
    for i, (x, h) in enumerate(zip(*[iter(XH)] * 2)):
        monster[i] = (x, (h + A - 1) // A)

    monster.sort()

    X = [x for x, h in monster]
    S = [0] * (N + 1)
    idx = 0
    ans = 0

    for i, (x, h) in enumerate(monster):
        d = h - S[i]
        if d > 0:
            right = x + 2 * D
            while idx < N and X[idx] <= right:
                idx += 1

            S[i] += d
            S[idx] -= d
            ans += d

        S[i + 1] += S[i]

    print(ans)
    return


if __name__ == '__main__':
    main()
