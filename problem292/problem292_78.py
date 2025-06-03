n=int(input())
d=list(map(int,input().split()))
sum1=sum(d)
sum2=0
for i in d:
    sum2+=i**2
print((sum1**2-sum2)//2)