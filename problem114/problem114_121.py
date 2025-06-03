def read_input():
    D = int(input())
    C = input().split()
    C = [int(i) for i in C]
    S = [list(map(int, input().split())) for _ in range(D)]
    T = [int(input()) for _ in range(D)]
    return D, C, S, T


def scoring(S, D, T, C):
    res = []
    last = [0 for _ in range(26)]
    final = 0
    for i in range(D):
        dec = 0
        last[T[i] - 1] = i + 1
        for j in range(26):
            dec += C[j] * (i - last[j] + 1)
        final += S[i][T[i] - 1] - dec
        res.append(final)
    return res


D, C, S, T = read_input()
res = scoring(S, D, T, C)
for x in res:
    print(x)
