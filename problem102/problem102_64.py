n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(0,n-k):
    if a[i]<a[k+i]:print("Yes")
    else :print("No")