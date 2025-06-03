n=int(input())
ans=0
for i in range(n):
    if (i+1)%3==0 and (i+1)%5==0:
        continue
    elif (i+1)%3==0:
        continue
    elif (i+1)%5==0:
        continue
    else:
        ans+=i+1
print(ans)