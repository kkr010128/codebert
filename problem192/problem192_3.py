from collections import Counter
N = int(input())
A = [int(i) for i in input().split()]

def comb(a):
    return a*(a-1)//2

m = Counter(A)
s = 0
ls = []
for a, b in m.items():
    s += comb(b)
for a in A:
    if m[a] == 1:
        ls.append(s)
    elif m[a] == 2:
        ls.append(s-1)
    else:
        ls.append(s-comb(m[a])+comb(m[a]-1))
print(*ls, sep='\n')