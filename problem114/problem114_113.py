def resolve():
    import numpy as np
    d = int(input())
    C = list(map(int, input().split()))
    S = []
    for _ in range(d):
        _S = list(map(int, input().split()))
        S.append(_S)
    S = np.array(S)

    T = []
    for _ in range(d):
        T.append(int(input()))

    last = [-1 for i in range(26)]
    score = 0
    for i in range(d):
        # max_idx = np.argmax(S[i])
        # print(max_idx + 1)
        score += S[i][T[i] - 1]
        last[T[i] - 1] = i
        for j in range(26):
            score -= C[j] * (i - last[j])

        print(score)

resolve()