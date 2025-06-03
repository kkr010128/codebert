import fractions
def c2(a):
    ans = 0
    while True:
        q,r = divmod(a,2)
        if r==0:
             ans+=1
             a = q
        else:break
    return ans
gcd =  fractions.gcd
n,m= map(int,input().split())
A = list(map(lambda x:int(x)//2,input().split()))
A.sort()
ma = 0
cp = c2(A[0])
for i in range(n):
    if cp!=c2(A[i]):
        print(0)
        exit()
lcm = A[0]
for i in range(1,n):
    lcm = A[i]*lcm//gcd(A[i],lcm)

print((m//lcm +1)//2)
