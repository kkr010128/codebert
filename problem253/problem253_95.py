n,a,b=map(int,input().split())
if (b-a)%2==0:
    print((b-a)//2);exit()
a-=1;b-=1
# print(min(b,n-1-a))
ans1=0; ans2=0
ans1+= a
aa=0 ; bb=b-a 
ans1+= (bb//2+1)

ans2=n-1-b 
b=n-1
a+=ans2
ans2+= (b-a)//2+1

print(min(ans1,ans2))