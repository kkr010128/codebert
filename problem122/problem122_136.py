n=int(input())
li=list(map(int,input().split()))
dic={}
ans=0
for i in range(n):
  val=dic.get(li[i],-1)
  if val==-1:
    dic[li[i]]=1
  else:
    dic[li[i]]=val+1
  ans+=li[i]
q=int(input())
for i in range(q):
  a,b=map(int,input().split())
  val=dic.get(a,-1)
  if val==-1 or val==0:
    print(ans)
  else:
    nb=dic.get(b,-1)
    if nb==-1:
      dic[b]=val
    else:
      dic[b]=val+nb
    ans+=(b-a)*val
    dic[a]=0
    print(ans)
  

   


  


