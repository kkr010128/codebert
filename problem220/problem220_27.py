S,T = input().split()
a,b = map(int,input().split())
u = input()

if u == S:
  a -= 1
elif u ==T:
  b -= 1
  
print("{} {}".format(a,b))