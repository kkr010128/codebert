from collections import defaultdict

n,x,y=map(int,input().split())
x-=1
y-=1
dic=defaultdict(int)
for i in range(n-1):
    for j in range(i+1,n):
        temp=min(j-i,abs(x-i)+1+abs(y-j),abs(x-j)+1+abs(y-i))
        dic[temp]+=1
for i in range(1,n): print(dic[i])