def comb(n):
    if n <= 1:
        return 0
    return n * (n - 1) // 2


def check(L):
    r = {}
    a = 0
    c = 0
    for i in range(len(L)):
        if a != L[i]:
            if i != 0:
                r[a] = [comb(c), comb(c - 1)]
            a = L[i]
            c = 1 
        else:
            c += 1
    r[a] = [comb(c), comb(c - 1)]
    #print(r)
    return r

N = int(input())
A = [int(n) for n in input().split(" ")]

D = {}
for i in range(len(A)):
    D[i] = A[i]

D = sorted(D.items(), key=lambda x: x[1])
V = {}
for i in range(len(D)):
    V[D[i][0]] = i

AA = sorted(A)
rr = check(AA)
ss = 0
for k, v in rr.items():
    ss += v[0]
#print(ss)

for k in range(N):
    index = A[k]
    a = rr[index][0] - rr[index][1]
    print(ss - a)
