a=int(input())
List=[]
for i in range(a):
  p,q=map(int,input().split())
  List.append([p-q,p+q])
List=sorted(List, key=lambda x:x[1])
ans=0
t=-10000000000
for i in range(a):
  if t<=List[i][0]:
    ans+=1
    t=List[i][1]
print(ans)