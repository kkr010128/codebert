n=int(input())
x=list(map(int,input().split()))
m=10**15
for i in range(101):
    t=x[:]
    s=sum(list(map(lambda x:(x-i)**2,t)))
    m=min(m,s)
print(m)