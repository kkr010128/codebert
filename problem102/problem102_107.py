n,k=map(int,input().split())
ar=list(map(int,input().split()))
for i in range(k,n):
    print("Yes" if ar[i]>ar[i-k] else "No")
