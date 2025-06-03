S = input()
N = len(S)

def kaibun(s):
    n = len(s)
    f_kaibun = True
    for i in range(int(n/2)):
        j = n-1-i
        if j <= i:
            break
        if s[i] != s[j]:
            f_kaibun = False
            break
    return f_kaibun

if kaibun(S) and kaibun(S[0:int(round((N-1)/2))]) and kaibun(S[int(round((N+3)/2))-1:N]):
    print('Yes')
else:
    print('No')