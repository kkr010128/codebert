n=int(input())
k=[1]
ans=[]
c=26
wa=0
while wa+c<n:
  k.append(c)
  wa+=c
  c=c*26
n=n-1-wa
for i in k[::-1]:
  ans.append(n//i)
  n=n%i
t=''
for i in ans: 
  t+=chr(97+i)
print(t)