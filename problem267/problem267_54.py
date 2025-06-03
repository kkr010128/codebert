N = int(input())
S = list(input())
ans = 0
for x in range(1000) :
    X = list(str(x).zfill(3))
    i = 0
    j = 0
    if X[0] in S[:N-2] :
        i = S.index(X[0])
    else :
        continue
    if X[1] in S[i+1:N-1] :
        j = S[i+1:N-1].index(X[1])+i+1
    else :
        continue
    if X[2] in S[j+1:N] :
        ans += 1
                        
print(ans)
