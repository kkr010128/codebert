ini = lambda : int(input())
inm = lambda : map(int,input().split())
inl = lambda : list(map(int,input().split()))
gcd = lambda x,y : gcd(y,x%y) if x%y else y
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

n,m = inm()
h = inl()
p = [True] * n
for i in range(m):
    a,b = inm()
    a -= 1
    b -= 1
    if h[a] >= h[b]:
        p[b] = False
    if h[b] >= h[a]:
        p[a] = False
ans = sum(p)
print(ans)