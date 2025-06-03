n=int(input())
s=list(input())
num=list(range(10))
for i in range(10):
    num[i]=str(num[i])
ans=0
for i in range(n-2):
    if len(num)==0:
        break
    if s[i] in num:
        num2=[str(_) for _ in range(10)]
        num.remove(s[i])
        for j in range(i+1,n):
            if len(num2)==0:
                break
            if s[j] in num2:
                num2.remove(s[j])
                ans+=len(set(s[j+1:]))
print(ans)
