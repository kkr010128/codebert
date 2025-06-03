N,M,K=map(int, input().split())

MOD=998244353

ans=0
temp2=1
#temp4=(M-1)**(N-1)%MOD

def getInvs(n, MOD):
  invs = [1] * (n+1)
  for x in range(2, n+1):
    invs[x] = (-(MOD//x) * invs[MOD%x]) % MOD
  return invs

invs = getInvs(max(N+3,M-1), MOD)

Vec=[0]*N
#inv=1
#for i in range(MOD-2):
#  inv*=M-1
#  inv%=MOD

'''
for i in range(K+1):
  if i == 0:
    temp1=M
    temp1*=(M-1)**(N-1)%MOD
    temp1%=MOD
    ans+=temp1*temp2%MOD
    #print(cmb)
  else:
    temp1*=invs[M-1]%MOD
    temp2*=(N-i)*invs[i]
    temp2%=MOD
    ans+=temp1*temp2%MOD
    cmb=cmb*(N-i-1)*i*invs[i]%MOD
    #print(cmb)
'''
for i in range(N):
  if i == 0:
    temp1=M
    Vec[N-i-1]=temp1
  else:
    temp1*=(M-1)*(N-i)
    temp1*=invs[i]
    temp1%=MOD
    Vec[N-i-1]=temp1


ans=sum(Vec[:K+1])

print(ans%MOD)
