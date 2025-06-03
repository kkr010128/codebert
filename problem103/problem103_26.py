



n=int(input())
a=list(map(int,input().split()))


res=1000

for i in range(1,n):

    if a[i]>a[i-1]:
        t=(res//a[i-1])*a[i]+res%a[i-1]
        res=t


print(res)