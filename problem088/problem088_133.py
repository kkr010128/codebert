n=int(input())
heights=list(map(int, input().split()))

std=heights.pop(0)
ans=0
if n==1:
  ans=0
else:
  for height in heights:
    if std>height:
      ans+=std-height
    else:
      std=height
print(ans)