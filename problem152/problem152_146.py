N = int(input())
S = list(input() for _ in range(N))
X = []
for s in S:
    l,r = 0,0
    for c in s:
        if c == ")":
            if r > 0:
                r -= 1
            else:
                l += 1
        else:
            r += 1
    X.append([l,r])
X.sort(key = lambda x:x[0])
Y = []
L = 0
for p,q in X:
    if p > L:
        print("No")
        quit()
    if q >= p:
        L -= p
        L += q
    else:
        Y.append([p,q])
Y.sort(key = lambda x:-x[1])
for a,b in Y:
    if a > L:
        print("No")
        quit()
    L -= a
    L += b
if L:
    print("No")
else:
    print("Yes")     