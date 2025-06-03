N = int(input())
a = list(map(int,input().split()))
dic = {}
for nums in a:
  if nums in dic:
    dic[nums] += 1
  else:
    dic[nums] = 1
ma = 0
for keys in dic:
  ma = max(ma,dic[keys])
if ma == 1:
  print("YES")
else:
  print("NO")