MOD=10**9+7
K=int(input())
S=list(input())
len_S=len(S)

def invmod(a):
  return pow(a,MOD-2,MOD)
fact_dic={0:1}
fact_inv_dic={0:1}
fact_mod=1
for i in range(1,K+len_S+1):
  fact_mod=(fact_mod*i)%MOD
  fact_dic[i]=fact_mod
  fact_inv_dic[i]=invmod(fact_mod)
def comb_mod_table(n,r):
  if 0<=r<=n:
    return fact_dic[n]*fact_inv_dic[r]*fact_inv_dic[n-r]
  else:
    return 0
  
pow25=pow(25,K,MOD)
inv25=invmod(25)
pow26=1
answer=0
for i in range(K+1):
  answer+=comb_mod_table(K+len_S-i-1,len_S-1)*pow25*pow26
  pow25=pow25*inv25%MOD
  pow26=pow26*26%MOD
  answer%=MOD
  
print(answer)