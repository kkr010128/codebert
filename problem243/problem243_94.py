N=int(input())
s=[0]*N
t=[0]*N
for i in range(N):
  s[i],t[i] = input().split()
  t[i]=int(t[i])
X=input()

j= s.index(X)
if X==s[-1]:
  ans=0
else:
  ans= sum(t[j+1:])

print(ans)