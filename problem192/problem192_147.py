def abc159d_banned_k():
    def cmb(n, r):
        """ nCrの組み合わせ数を返す """
        if n - r < r: r = n - r
        if r == 0: return 1
        if r == 1: return n

        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]

        for p in range(2,r+1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p-1,r,p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result *= int(numerator[k])

        return result
    n = int(input())
    a = list(map(int, input().split()))
    dict_a = {}
    for item in a:
        if item in dict_a.keys():
            dict_a[item] += 1
        else:
            dict_a[item] = 1
    cnt = 0
    for k in dict_a:
        if dict_a[k] > 1:
            cnt += cmb(dict_a[k],2)
    for item in a:
        if dict_a[item] > 2:
            print(cnt - cmb(dict_a[item],2) + cmb(dict_a[item]-1,2))
        elif dict_a[item] == 2:
            print(cnt - 1)
        else:
            print(cnt)

abc159d_banned_k()