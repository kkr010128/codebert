a,b,m=map(int,input().split())
ali= list(map(int,input().split()))	
bli= list(map(int,input().split()))	
min=min(ali)+min(bli)
for i in range(0,m):
  x,y,c=map(int,input().split())
  mon=ali[x-1]+bli[y-1]-c
  if mon<min:
    min=mon
    
print(min)