S = input()
K = int(input())

if(S.count(S[0]) == len(S)):
    print(len(S)*K//2)
else:
    cnt = 0
    lst = []
    tmp = S[0]
    for i in range(len(S)):
        if(tmp == S[i]):
            cnt += 1
        else:
            tmp = S[i]
            if(cnt > 1):
                lst.append(cnt)
            cnt = 1   
    if(cnt > 1):
        lst.append(cnt)
        
    ans = 0
    for i in lst:
        ans += K*(i//2)
    if(S[0] != S[-1]):
        print(ans)
    else:
        a = 0
        b = 0
        for i in range(len(S)):
            if(tmp != S[i]):
                break
            a += 1
        for i in S[::-1]:
            if(tmp != i):
                break
            b += 1
        print(ans+((a+b)//2-(a//2+b//2))*(K-1))