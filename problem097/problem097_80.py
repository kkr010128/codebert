K=int(input())
S=set()
ans=0

x=7%K
i=1
while True:
    if x==0:
        ans=1
        break
    if x in S:
        break
    else:
        S.add(x)
    x=(x*10+7)%K
    i+=1

print(i if ans else -1)