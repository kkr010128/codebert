n=int(input())
li=[]
ans=0
flug=0

for i in range(n):
    li.append(input().split())

x=input()

for j in range(n):
    if flug==0:
        if li[j][0]==x:
            flug=1
    else:
        ans+=int(li[j][1])

print(ans)