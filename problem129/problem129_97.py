n=int(input())
l=list(map(int,input().split()))
a=[0]*(10**6+1)
for i in range(n):
    if(a[l[i]]==0):
       for j in range(2*l[i],10**6+1,l[i]):
           a[j]=2
    a[l[i]]+=1
print(a.count(1))       
