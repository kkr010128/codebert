n=int(input())
a=list(map(int,input().split()))
temp=a[0]
for i in range(n-1):
    temp=temp^a[i+1]
for i in range(n):
    print(temp^a[i])