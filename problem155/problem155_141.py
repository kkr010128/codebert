import math
def facts(n):
    ans = []
    for  i in range(1, int(math.sqrt(n)+1)):
        if(n%i==0):
            ans.append(i)
            ans.append(n//i)
    ans = sorted(ans)
    return ans


n,m = map(int, input().split())
hs = list(map(int, input().split()))
state = [1 for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    if(hs[a-1]>=hs[b-1]):
        state[b-1] =0
    if(hs[a-1]<= hs[b-1]):
        state[a-1]= 0
ans = 0
for i in range(n):
    if(state[i]==1):
        ans+=1
print(ans)
