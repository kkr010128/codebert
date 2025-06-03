from sys import exit

def gcd(x,y):
    if x == 0: return y
    else: return gcd(y%x,x)


N = int(input())
A = list(map(int,input().split()))

is_prime = [True]*(10**6+10)
is_prime[0] = False
is_prime[1] = False

for i in range(2,10**6+10):
    if not is_prime[i]:
        continue
    else:
        for j in range(i*i,10**6+10,i):
            is_prime[j] = False

g = 0
for i in A:
    g = gcd(g,i)

if g != 1:
    print("not coprime")
    exit(0)

prime = [p for p in A if is_prime[p]]
used = [False]*(10**6+10)
notprime = [np for np in A if not is_prime[np]]
small_prime = [p for p in range(10**3+10) if is_prime[p]]


for p in prime:
    used[p] = True

for np in notprime:
    for p in small_prime:
        if np == 1: break
        if np % p != 0: continue
        if used[p]:
            print("setwise coprime")
            exit(0)
        used[p] = True
        while np % p == 0:
            np //= p
    if np > 1:
        if used[np]:
            print("setwise coprime")
            exit(0)
        used[np] = True

print("pairwise coprime") 