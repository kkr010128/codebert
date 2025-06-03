x,n= map(int,input().split())
p = list(map(int,input().split()))
ans=0
i=0
while True:
    if x-i not in p:
        ans=x-i
        break
    elif x+i not in p:
        ans=x+i
        break
    else:
        i+=1
        continue
print(ans)