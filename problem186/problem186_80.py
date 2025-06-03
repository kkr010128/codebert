k,n=map(int,input().split())
l=list(map(int,input().split()))

diff=[]
l.append(l[0]+k)
for i in range(n):
  diff.append(l[i+1]-l[i])

print(sum(diff)-max(diff))
