x = input().split()
a,b,c=[int(x) for x in x]
ans=0
for x in range(a,b+1):
    if c%x==0:ans+=1
print(ans)
