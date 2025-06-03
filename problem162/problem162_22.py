import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    ans = [[] for j in range(M)]

    if N % 2:
        for i in range(M):
            ans[i].append(i + 1)
            ans[i].append(N - i - 1)
    else:
        memo = 0
        f = False
        for i in range(M):
            memo = i
            if (i + 1) * 4 >= N:
                f = True
                break
            ans[i].append(i + 1)
            ans[i].append(N - i - 1)

        if f:
            for j in range(memo, M):
                ans[j].append(j + 1)
                ans[j].append(N - j - 2)
    for a in ans:
        print(*a)


if __name__ == '__main__':
    main()
