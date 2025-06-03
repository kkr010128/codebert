import math

def check( a,b ):
  g=math.ceil(a*100/8)
  
  for i in range(100):
      if b==int((g+i)*10/100):
          break
  
  if a!=int((g+i)*8/100):
      ans = "-1"
  else:
      ans = g+i
  return ans


a,b = map(int,input().split())
ans = check(a,b)
print(ans)