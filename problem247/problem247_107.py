import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a//gcd(a, b)*b

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = [ai//2 for ai in a]
cnt = [0]*N

for i in range(N):
    t = b[i]
    
    while t%2==0:
        cnt[i] += 1
        t //= 2
    
if cnt!=[cnt[0]]*N:
    print(0)
    exit()

L = 1

for bi in b:
    L = lcm(L, bi)

if L>M:
    print(0)
else:
    print((M-L)//(2*L)+1)