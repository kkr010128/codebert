n,x,t=map(int,input().split())
kaisu=n//x
if n%x!=0:
    kaisu+=1
ans=kaisu*t
print(ans)
