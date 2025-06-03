x=int(input())
next=[]
now=[1,2,3,4,5,6,7,8,9]

for _ in range(11):
  if x<=len(now):
    print(now[x-1])
    exit()
  else:
    x-=len(now)
    next=now
    now=[]
    for i in next:
      i=str(i)
      if i[-1]=='0':
        j=i+'0'
        k=i+'1'
        now+=[j]
        now+=[k]
      elif i[-1]=='9':
        j=i+'8'
        k=i+'9'
        now+=[j]
        now+=[k]
      else:
        j=i+str(int(i[-1])-1)
        k=i+str(int(i[-1]))
        l=i+str(int(i[-1])+1)
        now+=[j]
        now+=[k]
        now+=[l]