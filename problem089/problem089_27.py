def main():
    H, W, M = map(int, input().split())
    cnth = [[0, i] for i in range(H)]
    cntw = [[0, i] for i in range(W)]
    L = set()
    for _ in range(M):
        h, w = map(lambda x: int(x) - 1, input().split())
        cnth[h][0] += 1
        cntw[w][0] += 1
        L.add((h, w))
    cnth.sort(reverse=True)
    cntw.sort(reverse=True)
    mh = set()
    ph = cnth[0]
    for h in cnth:
        if ph[0] == h[0]:
            mh.add(h[1])
        else:
            break
        ph = h
    mw = set()
    pw = cntw[0]
    for w in cntw:
        if pw[0] == w[0]:
            mw.add(w[1])
        else:
            break
        pw = w
    maxans = cnth[0][0] + cntw[0][0]
    for h in mh:
        for w in mw:
            if not ((h, w) in L):
                print(maxans)
                break
        else:
            continue
        break
    else:
        print(maxans - 1)
if __name__ == "__main__":
    main()