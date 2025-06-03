n=int(input())
l=list(map(int,input().split()))
d=[0]*(n+1)
for i in l:
    d[i]+=1
for i in range(1,n+1):
    print(d[i])
