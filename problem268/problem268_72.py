import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 1
    mod = 10 ** 9 + 7
    for i in range(n):
        A[i] += 1

    cnt = [0] * (n + 1)  # cnt[i]は、Aのなかでこれまでに何個iが登場したか。つまりiの候補数。
    cnt[0] = 3

    for j in range(n):
        i = A[j]
        ans *= cnt[i - 1]
        cnt[i - 1] -= 1
        cnt[i] += 1
        if cnt[i] > 3:
            ans = 0
        if cnt[i - 1] < 0:
            ans = 0
    print(ans % mod)


resolve()