n=int(input())
b=input().split()
s=b[:]
for i in range(n):
    for j in range(n-1,i,-1):
        if b[j][1]<b[j-1][1]:b[j],b[j-1]=b[j-1],b[j]
    m=i
    for j in range(i,n):
        if s[m][1]>s[j][1]:m=j
    s[m],s[i]=s[i],s[m]
print(*b)
print('Stable')
print(*s)
print(['Not stable','Stable'][b==s])