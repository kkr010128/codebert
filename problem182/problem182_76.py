n,k,c=map(int,input().split())
s=input()
def greedy_work(days,rest,plan):
  day_count=0
  go=[0]*n
  while day_count < days:
    if plan[day_count]=='o':
      go[day_count]=1
      day_count += rest+1
    else:
      day_count += 1
  return(go)
front = greedy_work(n,c,s)
back = greedy_work(n,c,s[::-1])
back = back[::-1]
if front.count(1)==k:
  for i in range(n):
    if front[i]==1 and back[i]==1:
      print(i+1)