n=int(input())
l=[]
ll=[]
for i in range(n):
  x,y=map(int,input().split())
  l.append(x+y)
  ll.append(x-y)

l.sort()
ll.sort()

print(max(l[-1]-l[0],ll[-1]-ll[0]))
