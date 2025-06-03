N,P = map(int,input().split())
S = input()

def solve(S,N,P):
    if P == 2:
        ans = 0
        for i in range(N):
            if int(S[i])%P == 0:
                ans += i+1
        return ans
    if P == 5:
        ans = 0
        for i in range(N):
            if int(S[i])%P == 0:
                ans += i+1
        return ans
    
    S = S[::-1]
    mod_list = [0]*P
    mod_list[0] = 1

    mod = P
    tmp = 0

    for i in range(N):
        tmp = (tmp + int(S[i])*pow(10,i,mod))%mod
        mod_list[tmp] += 1
    
    ans = 0
    for i in mod_list:
        ans += i*(i-1)//2
        
    return ans

print(solve(S,N,P))