
def solve(S,K):
    if all(S[0]==c for c in S):
        return (len(S)*K)//2

    if S[0] == S[-1]:
        cnt0 = 0
        for c in S:
            if c == S[0]:
                cnt0 += 1
            else:
                break
        cnt1 = 0
        for c in reversed(S):
            if c == S[0]:
                cnt1 += 1
            else:
                break
        res = cnt0//2 + cnt1//2 - (cnt0+cnt1)//2
        S = S[cnt0:]+S[:cnt0]
    else:
        res = 0

    t = 0
    k = 0
    last = S[0]
    for c in S:
        if c == last:
            k += 1
        else:
            t += k//2
            k = 1
            last = c
    t += k//2
    res += t*K
    return res

S = input()
K = int(input())
print(solve(S,K))