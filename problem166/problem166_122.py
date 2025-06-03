s=[int(_) for _ in input()]

m = [0 for i in range(2019)]

d=0
m[d]+=1
p=1
for i in range(len(s)):
  d=(d+s[-i-1]*p)%2019
  m[d]+=1
  p=(p*10)%2019
  #print(d)


ans=0  
for i in range(2019):
  ans+=m[i]*(m[i]-1)//2
  
print(ans)