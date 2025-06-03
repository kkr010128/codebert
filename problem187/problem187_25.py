n,x,y=map(int,input().split())
a=[0]*n
for i in range(1,n+1):
    for j in range(i,n+1):
        b=min(abs(i-j),abs(i-x)+1+abs(y-j),abs(x-j)+1+abs(y-i))
        a[b]+=1
print(*a[1:],sep="\n")