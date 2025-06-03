N,X,Y=map(int,input().split())
d=[0]*N
for i in range(N):
 for j in range(i+1,N):d[min(j-i,abs(X-1-i)+abs(Y-1-j)+1)]+=1
for i in d[1:]:print(i)
