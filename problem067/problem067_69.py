n = int(input())
a = 0
b = 0
for i in range(n):
  t1,t2 = input().split()
  if t1>t2:
    a+=3
  elif t1==t2:
    a+=1
    b+=1
  else:
    b+=3
print(a,b)
