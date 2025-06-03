s=list(input())
t=list(input())
ans=[]

for i in range(len(s)-len(t)+1):
    u=s[i:len(t)+i]
    a=0
    for j in range(len(t)):
        if not t[j-1]==u[j-1]:
            a=a+1
    ans.append(a)
print(min(ans))