S = list(input())
K = int(input())

if len(set(S)) == 1:
    print(len(S)*K //2)
else:
    cnt = [1]
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt[-1] += 1
        else:
            cnt.append(1)
    
    res = 0
    for c in cnt:
        res += c//2*K

    if S[0] == S[-1]:
        if (cnt[0]+cnt[-1])%2 == 0:
            res += K-1
    
    print(res)