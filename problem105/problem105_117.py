n=int(input())
a=list(map(int,input().split()))
d=0
for i in range(0,n,2):
    if a[i]%2==1:
        d+=1
print(d)