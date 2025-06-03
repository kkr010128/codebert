n=int(input())
a=list(map(int,input().split()))
sum_a=sum(a)
x=0
i=0
while x<sum_a/2:
    x+=a[i]
    i+=1
if n%2==0:
    print(min(x-(sum_a-x),sum_a-(x-a[i-1])*2))
else:
    print(x-(sum_a-x))