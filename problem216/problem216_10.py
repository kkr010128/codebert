a,b,c = map(int, input().split())

ans = "No"

if (a == b or a== c or b == c) and not (a==b==c): ans = "Yes"
  
print(ans)
