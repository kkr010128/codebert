p = 10**9+7
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*(pow(x,(m-1)//2)**2)%p)%p
A = [1 for _ in range(10001)]
for i in range(2,10001):
    A[i] = (i*A[i-1])%p
B = [1 for _ in range(10001)]
B[10000] = pow(A[10000],p-2)
for i in range(9999,1,-1):
    B[i] = ((i+1)*B[i+1])%p
def f(n,k):
    if k>n:
        return 0
    return (A[n]*B[k]*B[n-k])%p
S = int(input())
n = S//3
ans = 0
for i in range(n,0,-1):
    k = S-3*i
    ans = (ans+f(k+i-1,i-1))%p
print(ans)