N,K = map(int, input().split())
A = [int(a) for a in input().split()]

S = [0]*(N+1)
for i in range(N):
    S[i+1] = (S[i] + A[i]) % K
    
for i in range(N+1):
    S[i] = (S[i] - i) % K
    
dic = {}
for i in range(min(K, N+1)):
    if S[i] in dic:
        dic[S[i]] += 1
    else:
        dic[S[i]] = 1
        

ans = 0
for key in dic:
    ans += dic[key]*(dic[key]-1)//2
    
if K < N+1:
    for i in range(K, N+1):
        dic[S[i-K]] -= 1
        if S[i] in dic:
            ans += dic[S[i]]
            dic[S[i]] += 1
        else:
            dic[S[i]] = 1
            
print(ans)