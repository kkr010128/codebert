n=int(input())
X=input()
x=X.count('1')
x_plus=int(X,2)%(x+1)
keta=n-1
if x==1:
    for i in range(n):
        tmp=0
        ans=1
        if X[i]=='0':
            tmp+=x_plus
            tmp+=pow(2,keta,(x+1))
            tmp%=(x+1)
            while tmp:
                tmp=tmp%(bin(tmp).count('1'))
                ans+=1
            print(ans)
        else:
            print(0)
        keta-=1
else:
    x_minus=int(X,2)%(x-1)
    for i in range(n):
        tmp=0
        ans=1
        if X[i]=='0':
            tmp+=x_plus
            tmp+=pow(2,keta,(x+1))
            tmp%=(x+1)
            while tmp:
                tmp=tmp%(bin(tmp).count('1'))
                ans+=1
            print(ans)
        else:
            tmp+=x_minus
            tmp-=pow(2,keta,(x-1))
            tmp%=(x-1)
            while tmp:
                tmp=tmp%(bin(tmp).count('1'))
                ans+=1
            print(ans)
        keta-=1