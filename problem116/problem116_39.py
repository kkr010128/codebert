S = list(input())
T = list(input())
L = len(S)

i = 0
cn = 0
N = 200000



while i < L:
    if S[i] != T[i]:
        i = i + 1
        cn = cn + 1
    else:
        i = i + 1

print(cn)