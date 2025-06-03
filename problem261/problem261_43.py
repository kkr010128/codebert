a=str(input());ans=0
for i in range(len(a)//2):
    if a[i]!=a[len(a)-i-1]:
        ans+=1
print(ans)