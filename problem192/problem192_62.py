n = int(input())
a = [0]+[int(x) for x in input().split()]

kosuu=[0]*(n+10)
kumiawase=[0]*(n+10)


for i in a:
    kosuu[i]+=1

for i in range(n+1):
    if kosuu[i]>0:
        kumiawase[i]=(kosuu[i]*(kosuu[i]-1))/2

ans=sum(kumiawase)
for i in range(1,n+1):
    print(int(ans-(kosuu[a[i]]-1)))