l,R, d = map(int, input().split())

a =0
for i in range(l,R+1):
  if i % d == 0:
    a = a+1 

print(a)
