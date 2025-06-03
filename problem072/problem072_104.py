c=int(input())
ans=0
now=0
for _ in range(c):
  if eval(input().replace(" ","==")):
    now = now+1
  else:
    now = 0
  ans = max(ans,now)
print("Yes") if ans >= 3 else print("No")