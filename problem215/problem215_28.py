N,K=map(int, raw_input().split())
 
mod=10**9+7
fact, inv_fact = [1], [1]
fact_tmp = 1
for i in range(1,N+1):
    fact_tmp *= i
    fact_tmp %= mod
    fact.append(fact_tmp)
    inv_fact.append(pow(fact_tmp, mod-2, mod))
 
def ncr(n,r):
	if n < 0 or r < 0 or n < r:	return 0
	else:	return (fact[n] * inv_fact[r] * inv_fact[n-r]) %mod

can_zero_num=min(N-1,K)
ans=0
for zero_num in range(can_zero_num+1):
    ans+=ncr(N,zero_num)*ncr(N-1,N-zero_num-1)

print ans%mod