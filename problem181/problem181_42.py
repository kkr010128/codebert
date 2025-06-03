k=int(input())

que=list(range(1,9+1))

while True:
  if len(que)>=k:
    break
  k-=len(que)
  for q in que[:]:
    que.remove(q)
    lq=int(str(q)[-1])
    for r in (lq-1,lq,lq+1):
        if 0<=r<=9:
            que.append(int(str(q)+str(r)))
 
  if len(que)>=k:
    break
 
que.sort()
print(que[k-1])