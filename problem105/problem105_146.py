N=int(input())

a=[int(x) for x in input().split()]
count=0
for i in range(len(a)):
    if (i+1)%2==1 and a[i]%2==1:
        count=count+1

print(count)

