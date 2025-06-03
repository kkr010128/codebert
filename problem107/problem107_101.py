N = int(input())
X = input()

def f(x):
    ret = 0
    c = bin(x).count("1")
    while c > 0:
        x %= c
        c = bin(x).count("1")
        ret += 1
    return ret

MOD = 10 ** 9 + 7
origin_pop = X.count("1")
one_pop = origin_pop - 1
zero_pop = origin_pop + 1
one_mod = 0
zero_mod = 0

for i in X:
    if one_pop > 0:
        one_mod = one_mod * 2 + int(i)
        one_mod %= one_pop
    zero_mod = zero_mod * 2 + int(i)
    zero_mod %= zero_pop

for i, x in enumerate(X):
    if x == "0":
        tmp = zero_mod + pow(2, N-1-i, zero_pop)
        tmp %= zero_pop
        print(f(tmp)+1)
    else:
        if one_pop == 0:
            print(0)
        else:
            tmp = one_mod - pow(2, N-1-i, one_pop)
            tmp = (tmp + one_pop) % one_pop
            print(f(tmp)+1)
