import sys
K=input()
if int(K)%2==0:
    print(-1)
    sys.exit()

S=int('7'*(len(K)))
ans=len(K)
K=int(K)
for i in range(10**6):
    if S%K==0:
        print(ans)
        break
    else:
        S=(S*10)%K+7
        ans+=1
else:
    print(-1)