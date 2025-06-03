n = int(input())
l = sorted(list(map(int,input().split())))
ans = 0
for ai in range(n):
  for bi in range(ai+1,n):
    ok,ng = bi,n
    while ng-ok>1:
      mid = (ng+ok)//2
      if l[mid]<l[ai]+l[bi]:
        ok = mid
      else:
        ng = mid
    ans += ok-bi
print(ans)