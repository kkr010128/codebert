N = int(input())
pl = []
mi = []

for i in range(N):
    _m = 0
    _t = 0
    s = input()
    for c in s:
        if c == ")":
            _t -= 1
            _m = min(_m, _t)
        else:
            _t += 1
    if _t > 0:
        pl.append([-_m, -_t]) # sortの調整のために負にしている
    else:
        mi.append([- _t + _m,  _m, _t])
pl = sorted(pl)
mi = sorted(mi)

#import IPython;IPython.embed()


if len(pl) == 0:
    if mi[0][0] == 0:
        print("Yes")
    else:
        print("No")
    exit()
if len(mi) == 0:
    print("No")
    exit()

tot = 0
for m, nt in pl:
    if tot - m < 0: # これはひくではないのでは?
        print("No")
        exit()
    else:
        tot -= nt
for d, m, nt in mi:
    if tot + m <0:
        print("No")
        exit()
    else:
        tot += nt
if tot != 0:
    print("No")
else:
    print("Yes")
        



# どういう時できるか
# で並べ方
# tot, minの情報が必要
# totが+のものはminとtotを気をつける必要がある
# minがsum以上であればどんどん足していけばいい.
# なのでminが大きい順にsortし,totの大きい順にsort
# その次はtotがminusの中ではminが小さい順に加える
# 合計が0になる時Yes,それ意外No.