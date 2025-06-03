n,x,y=map(int,input().split())
x-=1;y-=1
fl=[0 for i in range(n-1)]
for i in range(n):
    for j in range(i+1,n):
        fl[min(abs(j-i),abs(j-x)+1+abs(y-i),abs(i-x)+1+abs(y-j))]+=1
print(*fl[1:],sep="\n")
print(0)
