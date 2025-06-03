a,b=map(int,input().split())
m=min(a,b)
kouyakusuu=1
for i in range(1,m+1):
    if a%i==0 and b%i==0:
        kouyakusuu=i
print(a*b//kouyakusuu)