S = input()
kuri = False
ans = 0
for i in range(len(S)-1, -1, -1):
    K = int(S[i])
    if kuri:
        K += 1
    kuri = False
    if K < 5:
        ans += K
    elif K > 5:
        ans += (10-K)
        kuri = True
    elif K == 5:
        if i > 0:
            M = int(S[i-1])
            if i != 0 and M >= 5:
                kuri = True
        ans += 5
    if i == 0 and kuri:
        ans += 1
print(ans)
