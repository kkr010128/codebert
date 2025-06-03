def kaibun(lst):
    k = len(lst)//2 + len(lst)%2
    for i in range(1,k+1):
        if lst[i-1] != lst[-i]:
            return False

    return True
S = list(input())
N = len(S)
if kaibun(S) and kaibun(S[:(N-1)//2]) and kaibun(S[(N+3)//2-1:]):
    print('Yes')

else:
    print('No')