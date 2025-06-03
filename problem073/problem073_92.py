import collections
MAXN = 10**6+10
sieve = [i for i in range(MAXN+1)]
p = 2
while p*p <= MAXN:
    if sieve[p] == p:
        for q in range(2*p,MAXN+1,p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1
    
def prime(a):
    tmp = []
    while a > 1:
        tmp.append(sieve[a])
        a //= sieve[a]
    return collections.Counter(tmp)
 
def main():
    N = int(input())
    ans = 0
    for c in range(1, N):
        p = prime(N - c)
        tmp = 1
        for v in p.values():
            tmp *= (v + 1)
        ans += tmp
    return ans
 
if __name__ == '__main__':
    print(main())