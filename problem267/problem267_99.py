n=int(input())
s=input()
ans=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            tar=str(i)+str(j)+str(k)
            now=0
            for l in range(n):
                
                if tar[0+now]==s[l]:now+=1
                if now==3:
                    ans+=1
                    break
print(ans)                    