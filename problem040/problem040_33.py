a,b,c = map (int,input().split())

if b < a :
  a , b = b , a
  
if c < a :
  a , c = c , a
  
if c < b :
  b , c = c , b
  
print(a,b,c)
