n=int(input())
a=list(map(int,input().split()))
mini=a[0]
count=0
for i in range(n):
    if mini>=a[i]:
        count+=1
        mini=a[i]
    else:
        pass
print(count)