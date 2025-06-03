n,k=map(int,input().split())
l=[0]*n
for i in range(k):
    x=int(input())
    d=list(map(int,input().split()))
    for i in d:
        l[i-1]+=1
c=0
for i in l:
    if(i==0):
        c=c+1
print(c)
