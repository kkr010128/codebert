def solve():
    H, W, M = map(int, input().split())
    N = 3 * 10 ** 5
    cnth = [0] * N
    cntw = [0] * N
    st = set()
    for i in range(M):
        h, w = map(lambda x: int(x) - 1, input().split())
        cnth[h] += 1
        cntw[w] += 1
        st.add((h, w))
    mh = max(cnth)
    mw = max(cntw)
    Y = []
    X = []
    for i in range(H):
        if cnth[i] == mh:
            Y.append(i)
    for i in range(W):
        if cntw[i] == mw:
            X.append(i)
    for y in Y:
        for x in X:
            if not (y, x) in st:
                return mh + mw
    return mh + mw - 1

print(solve())
