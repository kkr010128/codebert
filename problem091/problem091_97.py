petern = 0
n = input()
Ln = input()
L = list(map(int, Ln.split(' ')))
for i in range(0, len(L)) :
    moji1 = L[i]
    for j in range(i+1, len(L)):
        moji2 = L[j]
        for k in range(j+1, len(L)):
            moji3 = L[k]
            if moji1 != moji2 and moji2 != moji3 and moji3 != moji1 :
                if moji1+moji2 > moji3 and moji2+moji3 > moji1 and moji3+moji1 > moji2 :
                    petern += 1
print(petern)
