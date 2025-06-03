def main():
    h, w, m = map(int, input().split())
    hp = [0]*h
    wp = [0]*w
    hw = set()
    for _ in range(m):
        h1, w1 = map(int, input().split())
        hp[h1-1] += 1
        wp[w1-1] += 1
        hw.add((h1, w1))

    h_max = max(hp)
    w_max = max(wp)

    hh = [i+1 for i, v in enumerate(hp) if v == h_max]
    ww = [i+1 for i, v in enumerate(wp) if v == w_max]
    ans = h_max + w_max

    for hb in hh:
        for wb in ww:
            if (hb, wb) not in hw:
                print(ans)
                exit()
    print(ans-1)


if __name__ == '__main__':
    main()