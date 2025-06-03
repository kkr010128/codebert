import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *A = map(int, read().split())

    pos = [a for a in A if a >= 0]
    neg = [a for a in A if a < 0]

    pos.sort()
    neg.sort(reverse=True)

    if N == K:
        vec = A
    elif N == len(neg):
        if K & 1:
            vec = neg[:K]
        else:
            vec = neg[-K:]
    else:
        ans_pos = []
        ans_neg = []
        for _ in range(K):
            if not pos:
                ans_neg.append(neg.pop())
            elif not neg:
                ans_pos.append(pos.pop())
            elif pos[-1] > -neg[-1]:
                ans_pos.append(pos.pop())
            else:
                ans_neg.append(neg.pop())

        if (len(ans_neg) & 1) and ((not ans_pos) or (ans_pos[-1] != 0)):
            if not pos or not ans_neg:
                drop_pos = True
            elif not neg or not ans_pos:
                drop_pos = False
            else:
                drop_pos = pos[-1] * ans_pos[-1] < neg[-1] * ans_neg[-1]

            if drop_pos:
                ans_neg.append(neg.pop())
                ans_pos.pop()
            else:
                ans_pos.append(pos.pop())
                ans_neg.pop()

        vec = ans_pos + ans_neg

    ans = 1
    for a in vec:
        ans = ans * a % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
