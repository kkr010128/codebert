def n_cand(x):
    return int(x*1.08)

n = int(input())

x = round(n / 1.08)
n_dash = n_cand(x)
n_dash_m = n_cand(x-1)
n_dash_p = n_cand(x+1)
if n_dash == n:
    print(x)
elif n_dash_m == n:
    print(x-1)
elif n_dash_p == n:
    print(x+1)
else:
    print(':(')