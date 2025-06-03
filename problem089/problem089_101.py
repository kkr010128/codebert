def main():

    H, W, M = map(int, input().split())
    h_dic = [0] * H
    w_dic = [0] * W
    boms = set()
    for _ in range(M):
        h, w = map(int, input().split())
        h, w = h-1, w-1
        h_dic[h] += 1
        w_dic[w] += 1
        boms.add((h, w))

    hmax = max(h_dic)
    wmax = max(w_dic)

    h_maxs = [idx for idx, v in enumerate(h_dic) if v==hmax]
    w_maxs = [idx for idx, v in enumerate(w_dic) if v==wmax]

    # 爆弾数はたかだか3*10~5なので、総当りで解ける
    for h in h_maxs:
        for w in w_maxs:
            if (h, w) not in boms:
                print(hmax + wmax)
                return
    print(hmax + wmax - 1)
    return

if __name__ == "__main__":
    main()
