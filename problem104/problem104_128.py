L, R, d = map(int, input().split())
a = 0

for i in range(L,R+1):
  if i%d==0:
    a += 1
  else:
    a += 0

print(a)