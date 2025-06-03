n=int(input())
s=input()
ans=0
r,g,b=0,0,0
for i in range(n):
    if s[i]=="R":
        r+=1
    elif s[i]=="G":
        g+=1
    else:
        b+=1
for i in range(1,n):
    for j in range(i+1,n):
        if (j-i)+j<=n:
            k=(j-i)+j-1
            if  s[i-1]!=s[j-1] and  s[j-1]!=s[k] and s[k]!=s[i-1]:
                ans-=1
ans+=r*g*b
print(ans)