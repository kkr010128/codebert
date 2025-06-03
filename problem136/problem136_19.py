from collections import Counter

def prime_fact(n):
    P = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            P.append(i)
            n //= i
    if n != 1:
        P.append(n)
    return P
  
n = int(input())
cnt = Counter(prime_fact(n))
#print(cnt)

ans = 0
for c in cnt.values():
    tmp = 1
    while c >= tmp:
        c -= tmp
        ans += 1
        tmp += 1
        
print(ans)