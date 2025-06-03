N,M,Q=map(int,input().split())

abcd=[]
for i in range(Q):
  abcd.append(list(map(int,input().split())))
  abcd[i][0]-=1
  abcd[i][1]-=1

  
def calcScore(target):
  score=0
  for i in range(Q):
    if target[abcd[i][1]]-target[abcd[i][0]]==abcd[i][2]:
      score+=abcd[i][3]
  return score

def makeTarget():
  list=[1]*N
  list[-1]=0
  while True:
    list[-1]+=1
    for i in range(len(list)):
      if list[-i-1]>M:
        if len(list)==i+1:return
        list[-i-2]+=1
        list[-i-1]=0
    for i in range(len(list)-1):
      if list[i]>list[i+1]:list[i+1]=list[i]
    yield list.copy()

ans=0
for i in makeTarget():
  ans=max(ans,calcScore(i))
print(ans)