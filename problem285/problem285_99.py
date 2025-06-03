# A - ><
S = input()
N = len(S)+1
INF = 1000000
ans = [0]*N
tmp = 0
for i in range(N-1):
    if S[i]=='<':
        tmp += 1
    else:
        tmp = 0
    ans[i+1] = tmp
tmp = 0
for i in range(N-2,-1,-1):
    if S[i]=='>':
        tmp += 1
    else:
        tmp = 0
    ans[i] = max(ans[i],tmp)
print(sum(ans))