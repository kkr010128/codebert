from fractions import gcd
n,m = map(int,input().split())
a = list(map(lambda x: int(x)//2,input().split()))
def lcm(x,y):
    return x*y//gcd(x,y)
def f(x):
    cnt = 0
    while x%2 == 0:
        x //= 2
        cnt += 1
    return cnt
r = set([f(i) for i in a])
if len(r) != 1:
    print(0)
    exit()
T = 1
for i in range(n):
    T = lcm(T,a[i])
ans=-(-(m//T)//2)
c=T
print(ans)