n=int(input())
a=[int(x) for x in input().split()]
count=0
for i in range(0,n,2):
    if a[i]%2==1:
        count+=1
print(count)