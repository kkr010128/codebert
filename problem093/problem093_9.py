(n,k),p,c=[[*map(int,t.split())]for t in open(0)]
a=-9e9
for i in range(n):
 s=f=m=0;x,*l=i,
 while~f:x=p[x]-1;s+=c[x];l+=s,;m+=1;f-=x==i
 for j in range(min(m,k)):a=max(a,l[j]+(~j+k)//m*s*(s>0))
print(a)