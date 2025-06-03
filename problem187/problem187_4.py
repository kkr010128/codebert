n,x,y=map(int,input().split())

count=[0]*(n-1)
for i in range(n):
    l=i
    for j in range(i+1,n):
        r=j
        dis=min(j-i, abs(x-1-l)+1+abs(y-1-r))
        count[dis-1]+=1
        

for i in range(n-1):
    print(count[i])