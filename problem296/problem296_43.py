def f(s,n):
    res = 0
    flg = False
    for i in range(1,n):
        if flg:
            flg = False
            continue
        if S[i] == S[i-1]:
            flg = True
            res += 1
    return res
S = input()
K = int(input())
if len(set(list(S))) == 1:
    print(len(S)*K//2)
    exit()
ans = f(S,len(S))
S = S * 2
print(ans + (f(S,len(S)) - ans) * (K-1))