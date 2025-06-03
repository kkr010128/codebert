n=int(input())
a=[int(i) for i in input().split()]
sum=0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        sum=sum+(a[i]*a[j])
print(sum)