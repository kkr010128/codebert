import sys
N,K=map(int,input().split())
plist=[0]+list(map(int,input().split()))
clist=[-float("inf")]+list(map(int,input().split()))

if max(clist)<=0:
  print(max(clist))
  sys.exit(0)
  
if K<=N:
  max_answer=0
  for i in range(1,N+1):
    pos=i
    max_score=0
    score=0
    for c in range(K):
      pos=plist[pos]
      score+=clist[pos]
      max_score=max(score,max_score)
      
    #print(i,max_score)
    max_answer=max(max_answer,max_score)
    
  print(max_answer)
  sys.exit(0)
  
max_answer=0
for i in range(1,N+1):  
  pos=i
  cycle_list=[]
  score_list=[]
  for _ in range(N):
    pos=plist[pos]
    cycle_list.append(pos)
    score_list.append(clist[pos])    
    if pos==i:
      break
      
  num_cycle=K//len(cycle_list)
  cycle_score=sum(score_list)
  #print(cycle_list,score_list,num_cycle,cycle_score)
  
  score=0
  max_score=0  
  if cycle_score>=0:
    score+=(num_cycle-1)*cycle_score
  K2=K-len(cycle_list)*(num_cycle-1)

  for _ in range(K2):
    pos=plist[pos]
    score+=clist[pos]
    max_score=max(score,max_score)
  
  #print(i,max_score)
  max_answer=max(max_answer,max_score)
  
print(max_answer)