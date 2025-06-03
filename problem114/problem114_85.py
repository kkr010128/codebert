import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    D = int(input())
    C = list(map(int, input().split()))
    S = [list(map(int, input().split())) for _ in range(D)]
    T = list(int(input()) for _ in range(D))

    sat = 0
    last = [0] * 26
    for d in range(D):
        t = T[d] - 1
        sat += S[d][t]
        dsat = 0
        for i in range(26):
            if i == t:
                continue
            dsat += C[i] * ((d + 1) - last[i])
        last[t] = d + 1
        sat -= dsat
        print(sat)


if __name__ == '__main__':
    resolve()
