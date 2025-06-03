def factorize(n):
    tmp = n

    for i in range(2, int(n**0.5)+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            if i in fact:
                fact[i] = max(fact[i],cnt)
            else:
                fact[i] = cnt
         
    if tmp != 1:
        if tmp in fact:
            fact[tmp] = max(fact[tmp],1)
        else:
            fact[tmp] = 1
    
    if len(fact) == 0:
        if N in fact:
            fact[N] = max(fact[N],1)
        else:
            fact[N] = 1

def inv(n, p):
    return pow(n, p-2, p)
    
N = int(input())
A = list(map(int, input().split()))
p = 10**9+7

fact = {}

for i in range(N):
    if A[i] != 1:
        factorize(A[i])

lcm = 1

for key, val in fact.items():
    lcm *= pow(key, val, p)
    lcm %= p

inv_sum = 0

for i in range(N):
    inv_sum += inv(A[i], p)
    inv_sum %= p

print(lcm * inv_sum % p)