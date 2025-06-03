N,K,C = map(int,input().split())
S = list(input())
F = []
maru = 0
last = -10**9
span = C
for i in range(N):
    if S[i]=="o" and span >= C:
        maru += 1
        last = i
        F.append([maru,last])
        span = 0
    else:
        span += 1
        F.append([maru,last])
#print(F)
s = S[::-1]
maru = 0
last = 10**9
span = C
E = []
for i in range(N):
    if s[i] == "o" and span >= C:
        maru += 1
        last = N-1-i
        E.append([maru,last])
        span = 0
    else:
        E.append([maru,last])
        span += 1
E = E[::-1]
#print(E)
F = [[0,-10**9]] + F + [[0,10**9]]
E = [[0,-10**9]] + E + [[0,10**9]]
#print(F)
#print(E)
ans = []
for i in range(1,N+1):
    cnt = F[i-1][0] + E[i+1][0]
    
    if S[i-1] == "o":
        if E[i+1][1] - F[i-1][1] < C:
            cnt -= 1
        if cnt == K-1:
            ans.append(i)
    #print(F[i-1],E[i+1],cnt)
for i in range(len(ans)):
    print(ans[i])