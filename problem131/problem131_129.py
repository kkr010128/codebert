p1 , s1=map(int , input().split()) 
p2 , s2=map(int , input().split())
t=int(input()) 
if abs(p1-p2) > t*(s1-s2):
  print("NO")
else:
  print("YES")