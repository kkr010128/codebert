n=int(input())
s=input()

ans="No"
if n%2==0:
    p=n//2
    if s[:p]==s[p:]:
        ans="Yes"

print(ans)