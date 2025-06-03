import sys
input = sys.stdin.readline

def f(n):
    s = (n*(n+1))//2
    return s


N,K = map(int,input().split())
m= 10**9+7
ln = list(range(N+1))
num = 0
for i in range(K,N+2):
    num += f(N+1)-f(N+1-i)-f(i)+1
print(num%m)
    
