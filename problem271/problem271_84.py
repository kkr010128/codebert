N = int(input())
S = list(input())
L = [chr(ord("A")+i) for i in range(26)]
X = ""
for i in S:
    a = L.index(i) + N
    if a >= 26:
        a = a - 26
        X += L[a]
    else:
        X +=  L[a]
print(X)
