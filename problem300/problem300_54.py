def factorize(n):
    if n == 1:
        return
    
    tmp = n

    for i in range(2, int(n**0.5)+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            if i in fact:
                fact[i] = 1
            else:
                fact[i] = 0
         
    if tmp != 1:
        if tmp in fact:
            fact[tmp] = 1
        else:
            fact[tmp] = 0
    
    if len(fact) == 0:
        if N in fact:
            fact[N] = 1
        else:
            fact[N] = 0

A, B = list(map(int, input().split()))
fact = {}

factorize(A)
factorize(B)

cnt = 1

for val in fact.values():
    if val == 1:
        cnt += 1

print(cnt)