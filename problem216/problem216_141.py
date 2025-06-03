a,b,c=map(int,input().split())
ans="Yes"
if a==b==c :
    ans="No"
elif a!=b and b!=c and a!=c:
    ans="No"
print(ans)