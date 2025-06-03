from collections import Counter
a,b=map(int,input().split())
def p_fact(n):
  m=n
  i=2
  a=[1]
  while n>1:
    if i>m**.5:
      a+=[n]
      break
    if n%i==0:
      n//=i
      a+=[i]
    else:i+=1  
  return a
af,bf=p_fact(a),p_fact(b)
da,db={},{}
for i in af:
  if da.get(i):da[i]+=1
  else:da[i]=1
for i in bf:
  if db.get(i):db[i]+=1
  else:db[i]=1
dc={}
for i in da:
  if db.get(i):dc[i]=min(da[i],db[i])
print(len(dc))