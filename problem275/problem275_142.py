x,y = map(int, input().split())
ans = 0

dic = {1:300000, 2:200000, 3:100000}
if x in dic:
  ans = dic[x]
if y in dic:
  ans += dic[y]
  
if x==1 and y==1:
  ans += 400000
  
print(ans)