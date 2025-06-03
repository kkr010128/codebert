a,b,c=map(int, input().split())

if a==b and a!=c:
    ans="Yes"

elif a==c and a!=b:
    ans="Yes"

elif b==c and b!=a:
    ans="Yes"

else:
    ans="No"


print(ans)    
