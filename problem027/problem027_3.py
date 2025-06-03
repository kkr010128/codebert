import math

def koch(start,end,n):
  if n==0:
    return
  else:
    point1=[0,0]
    point2=[0,0]
    point3=[0,0]
    
    point1[0]=(end[0]-start[0])/3 +start[0]
    point1[1]=(end[1]-start[1])/3 +start[1]
    
    point3[0]=(end[0]-start[0])*2/3+start[0]
    point3[1]=(end[1]-start[1])*2/3+start[1]
    
    rad60 = math.radians(60)
    point2[0]=(point3[0]-point1[0])* math.cos(rad60) -(point3[1]-point1[1])*math.sin(rad60) +point1[0]
    point2[1]=(point3[0]-point1[0])* math.sin(rad60) +(point3[1]-point1[1])*math.cos(rad60) +point1[1]
    
    koch(start,point1,n-1)
    print(*point1)
    koch(point1,point2,n-1)
    print(*point2)
    koch(point2,point3,n-1)
    print(*point3)
    koch(point3,end,n-1)

n=int(input())

start=[0,0]
end=[100,0]

print(*start)

if n>0:
  koch(start,end,n)
  

print(*end)
