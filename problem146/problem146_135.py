def e_bullet(MOD=10**9 + 7):
    from math import gcd
    from collections import defaultdict
    N = int(input())

    zero_all = 0
    pair = defaultdict(int)
    for _ in range(N):
        a, b = [int(i) for i in input().split()]
        if a == 0 and b == 0:
            zero_all += 1
            continue

        g = gcd(a, b)
        if b == 0:
            pair[(1, 0)] += 1
        elif b > 0:
            pair[(a // g, b // g)] += 1
        else:
            pair[(-a // g, -b // g)] += 1

    is_checked = set()
    total = 1
    for (a, b), v in list(pair.items()):
        if (b, -a) in is_checked or (-b, a) in is_checked:
            continue  # a/b に対応するものがあるかはすでに調べた
        is_checked.add((a, b))
        # a/b に対応する b/(-a) か (-b)/a に注目する
        w = pair[(b, -a)] + pair[(-b, a)]
        # 両方を選ぶと仲が悪いので、a/b となるものだけ選ぶか [b/(-a) または (-b)/a]
        # となるものだけ選ぶか、どちらか一方だけ選択したときに仲が悪くならない
        # これまでの選び方に対して仲が悪くならない選び方を決めるので、total は積を取る
        # ただし、両方とも 1 つも選ばないということはできないため、-1 する
        total *= pow(2, v, MOD) + pow(2, w, MOD) - 1
        total %= MOD

    ans = (total + zero_all - 1) % MOD
    return ans

print(e_bullet())