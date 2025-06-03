from math import factorial
n,m=map(int,input().split())
ans=0
if n>1:
    ans+=factorial(n)//2//factorial(n-2)
if m>1:
    ans+=factorial(m)//2//factorial(m-2)
print(ans)