
def check(x,y):
  for i in range(100):
    for j in range(100):
        if i+j==x and i*4+j*2==y :
            return "Yes"
  return "No"

x,y = map(int, input().split())
print( check(x,y) )
