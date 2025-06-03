s=input()
t=input()
ans=int(len(s))
for i in range(len(s)-len(t)+1):
    now=int(0)
    for j in range(len(t)):
        if s[i+j]!=t[j]:
            now+=1
    ans=min(now,ans)
print(ans)