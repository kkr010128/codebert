S = input()
T = input()

def count_diff(s, t):
    N = 0
    for i, j in zip(s, t):
        if i != j:
            N += 1
    return N


ns = len(S)
nt = len(T)

res = nt
for i in range(ns - nt + 1):
    sub = S[i:i+nt]
    a = count_diff(sub, T)
    if a < res:
        res = a

print(res)