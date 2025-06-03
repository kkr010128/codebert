n = int(input())
ans = "No"
count = 0
for i in range(n):
    D1,D2 = map(int,input().split())
    count=count+1 if D1==D2 else 0
    ans="Yes"  if count>=3 else ans

print(ans)