import sys

sys.setrecursionlimit(10000000)
input=sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
    return a // gcd(a, b) * b

mod = 10**9+7

x=a[0]

for i in a[1:]:
    x=lcm(x,i)
ans=0
for i in range(n):
    ans+= x//a[i]

print(ans%mod)
