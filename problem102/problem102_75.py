n,k=map(int,input().split())
a=list(map(int,input().split()))
l=[0]*(n-k)
for i in range(n-k):
    l[i]=a[i+k]/a[i]
for i in range(n-k):
    if l[i]>1:
        print("Yes")
    else:
        print("No")