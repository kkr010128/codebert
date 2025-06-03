a,b=map(int,input().split())
e=[]
for _ in range(b):
  c=int(input())
  d=list(map(int,input().split()))
  for i in d:
    e.append(i)

f=set(e)
print(a-len(f))