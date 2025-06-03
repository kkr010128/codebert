n=int(input())
s=str(input())
ans="Yes"
if len(s)%2==1:
    ans="No"
for i in range(len(s)//2):
    if s[i]!=s[len(s)//2+i]:
        ans="No"
        break
print(ans)