x,k,d=list(map(int,input().split()))
if k>=abs(x)//d:
    y=abs(x)//d
    ans=abs(abs(x)-y*d)
    ans=abs(ans-((k-y)%2)*d)
else:
    ans=abs(abs(x)-k*d)
print(ans)