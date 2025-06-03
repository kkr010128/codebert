p_max = 100000 * 10000

nk = list(map(int, input().split()))
w = [int(input()) for i in range(nk[0])]


def search(pt):
    m = 0
    for j in range(nk[1]):
        weight = 0
        while weight + w[m] <= pt:
            weight += w[m]
            m += 1
            if m == nk[0]:
                return nk[0]
    return m


def main():
    st_p = p = 0
    en_p = p_max
    while en_p - st_p > 1:
        p = int((en_p + st_p) / 2)
        chk = search(p)
        if chk >= nk[0]:
            en_p = p
        else:
            st_p = p
    return en_p


if __name__ == '__main__':
    print(main())

