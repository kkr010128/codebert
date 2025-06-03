n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()
d={'r':p,'s':r,'p':s}
d_={'r':'p','s':'r','p':'s'}
s=0
for i in range(k):
  a=0
  z='0'
  t_=t[i::k]
  for a in range(len(t_)):
    if a==0:
      s+=d[t_[a]]
      z=d_[t_[a]]
      a+=1
    else:
      if z==d_[t_[a]]:
        z='0'
        a+=1
      else:
        s+=d[t_[a]]
        z=d_[t_[a]]
        a+=1
print(s)   
