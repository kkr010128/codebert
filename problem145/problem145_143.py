n,m=map(int,input().split())

ans=[0 for i in range(n+1)]

list_tonari=[[] for i in range(n+1)]

for i in range(m):
  a,b=map(int,input().split())
  list_tonari[a].append(b)
  list_tonari[b].append(a)
  
const=list()
const.append(1)

const_vary=list()


while True:
  const_vary=const
  const=[]
  
  while len(const_vary):
    get=const_vary.pop()
    
    for n in list_tonari[get]:
      if ans[n] ==0:
        ans[n]=get
        list_tonari[n].remove(get)
        const.append(n)
        
  if len(const)==0:
    break
    
print("Yes")
for n in ans[2:]:
  print(n)
