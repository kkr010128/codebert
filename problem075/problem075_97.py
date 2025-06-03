n, x, m = map(int, input().split())

mn = min(n, m)
P = [] # value of pre & cycle
sum_p = 0 # sum of pre + cycle
X = [False] * m # for cycle check

for _ in range(mn):
    if X[x]: break
    X[x]  = True
    P.append(x)
    sum_p += x
    x = x*x % m

if len(P) >= mn:
    print(sum_p)
    exit()

pre_len = P.index(x)
cyc_len = len(P) - pre_len
nxt_len = (n - pre_len) % cyc_len

cyc_num = (n - pre_len) // cyc_len

cyc = sum(P[pre_len:])
remain = sum(P[:pre_len + nxt_len])

print(cyc * cyc_num + remain)
