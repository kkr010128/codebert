def mitsui2019d_lucky_pin():
    import itertools
    n = int(input())
    s = input()
    cnt = 0
    for t in itertools.product(range(0, 10), repeat=2):
        si = ''.join(map(str,t))
        for i in range(n - 2):
            if si[0] != s[i]: continue
            for j in range(i + 1, n - 1):
                if si[1] != s[j]: continue
                ss = set(list(s[j+1:]))
                cnt += len(ss)
                break
            break
    print(cnt)


mitsui2019d_lucky_pin()