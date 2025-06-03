n=int(input())
a=list(map(int,input().strip().split()))[:n]
counter=0
for i in range (0,n,2):
    if(a[i]%2==1):
        counter+=1

print(counter)