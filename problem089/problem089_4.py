def main():
    H, W, M = (int(i) for i in input().split())
    hc = [0]*(H+1)
    wc = [0]*(W+1)
    maps = set()
    for _ in range(M):
        h, w = (int(i) for i in input().split())
        hc[h] += 1
        wc[w] += 1
        maps.add((h, w))
    mah = max(hc)
    maw = max(wc)
    ans = mah+maw
    hmaps = []
    wmaps = []
    for i, h in enumerate(hc):
        if mah == h:
            hmaps.append(i)
    for i, w in enumerate(wc):
        if maw == w:
            wmaps.append(i)

    if M < len(hmaps) * len(wmaps):
        # 爆破対象の合計が最大になるマスがM個より多ければ，
        # 必ず爆破対象がないマスに爆弾を置くことができる
        # 逆にM個以下なら3*10^5のループにしかならないので
        # このようにif文で分けなくても，必ずO(M)になるのでelse節のforを回してよい
        print(ans)
    else:
        for h in hmaps:
            for w in wmaps:
                if (h, w) not in maps:
                    print(ans)
                    return
        else:
            print(ans-1)


if __name__ == '__main__':
    main()
