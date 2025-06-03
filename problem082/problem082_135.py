from sys import stdin
input = stdin.readline

def Judge(S, T):
    ls = len(S)
    lt = len(T)
    m = 0
    for i in range(ls-lt+1):
        tmp = 0
        for j in range(lt):
            if S[i+j] == T[j]:
                tmp += 1
        if m < tmp:
            m = tmp
    return lt - m

S = input().strip()
T = input().strip()

print(Judge(S, T))