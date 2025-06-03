input()
*l,=map(int,input().split())
ans=0
for i in l:
    for j in l:
        ans+=i*j
print((ans-sum([pow(x,2) for x in l]))//2)