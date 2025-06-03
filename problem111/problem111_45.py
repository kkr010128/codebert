n = int(input())
a = list(map(int,input().split()))

sa = sorted(a,reverse=True)
ans = sa[0]
i = 2
for v in sa[1:]:
  if i >= n:
    break
  #print("i:{} ans:{}".format(i,ans))
  ans += v
  i += 1
  if i >= n:
    break
  #print("i:{} ans:{}".format(i,ans))
  ans += v
  i += 1

print(ans)
