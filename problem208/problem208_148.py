def resolve():
    N, M = list(map(int, input().split()))
    SC = [list(map(int, input().split())) for _ in range(M)]
    value = [None for _ in range(N)]
    for s, c in SC:
        if not (value[s-1] is None or value[s-1] == c):
            print(-1)
            return
        value[s-1] = c
    for i in range(N):
        if value[i] is None:
            if i == 0:
                if N > 1:
                    value[i] = 1
                else:
                    value[i] = 0
            else:
                value[i] = 0
    if N > 1 and value[0] == 0:
        print(-1)
    else:
        print("".join(map(str, value)))


if '__main__' == __name__:
    resolve()