X=int(input())
ans=0
for i in range(X,10**5+100):
    cond=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            cond=False
            break
    if cond:
        ans=i
        break

print(ans)