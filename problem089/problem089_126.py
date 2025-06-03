def main():
    import sys
    input = sys.stdin.readline

    h,w,m = map(int, input().split())
    h_count = [0 for _ in range(h)]
    w_count = [0 for _ in range(w)]
    pairs = set()

    for i in range (m):
        hi, wi = map(int, input().split())
        hi -= 1
        wi -= 1

        h_count[hi] += 1
        w_count[wi] += 1

        pairs.add((hi,wi))

    h_max = max(h_count)
    w_max = max(w_count)
    hk = list()
    wk = list()

    for index , hj in enumerate(h_count):
        if hj == h_max:
            hk.append(index)
    
    for index, wj in enumerate(w_count):
        if wj == w_max:
            wk.append(index)

    ans = h_max + w_max

    for _h in hk:
        for _w in wk:
            hw = (_h, _w)

            if hw in pairs:
                continue

            print(ans)
            exit()
    print(ans -1)

if __name__ == '__main__':
    main()

