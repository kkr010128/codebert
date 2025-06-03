import sys
from itertools import accumulate

read = sys.stdin.buffer.read


def main():
    N, *L = map(int, read().split())

    L.sort()
    max_L = L[-1]

    C = [0] * (max_L + 1)
    for l in L:
        C[l] += 1
    C = list(accumulate(C))

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if L[i] + L[j] > max_L:
                ans += N - j - 1
            else:
                ans += C[L[i] + L[j] - 1] - j - 1

    print(ans)
    return


if __name__ == '__main__':
    main()
