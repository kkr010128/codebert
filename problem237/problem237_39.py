n=int(input())
B=[]
for i in range(n):
  x,l=map(int,input().split())
  B.append([x-l,x+l])
B.sort(key=lambda x:x[1])
max_l=-10**18-5
ans=0
for b in B:
  if max_l <= b[0]:
    max_l = b[1]
    ans+=1
print(ans)