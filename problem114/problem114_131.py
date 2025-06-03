import numpy as np

D = int(input())
C = np.array(list(map(int, input().split())))
S = []
for i in range(D):
    s = list(map(int, input().split()))
    S.append(s)
S = np.array(S)
T = [int(input()) for _ in range(D)]

last = np.zeros(26, dtype=np.int64)


def decrease(d, last):
    res = np.sum(C * (d - last))
    # print(d, res, C * (d - last))
    return res


manzoku = 0
# kaisai = dict()

# print(S, T, C)
for day, t in enumerate(T):
    t -= 1
    manzoku += S[day, t]  # d 日目にタイプi のコンテストを開催した場合、満足度が S[d,i]増加することが予め分かっています。
    last[t] = day + 1
    manzoku -= decrease(day + 1, last)

    print(manzoku)

