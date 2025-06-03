n,m=map(int,input().split())
s=input()
ans=[]
w=n
while w:
    x=0
    for i in range(1,m+1):
        if w-i>=0 and s[w-i]=='0':
            x=i
    if x==0:
        print(-1)
        exit()
    else:
        ans.append(x)
        w-=x
print(*ans[::-1])
