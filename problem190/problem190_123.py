S=input()
N=len(S)
M=(N-1)//2
def iskaibun(T):
    K=len(T)
    for i in range(K):
        if T[i]==T[-i-1]:
            pass
        else:
            return False
    return True

if iskaibun(S) and iskaibun(S[:M]) and iskaibun(S[M+1:]):
    print("Yes")
else:
    print("No")
