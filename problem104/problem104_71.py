L,R,d = (input().split())
L = int(L)
R = int(R)
d = int(d)
count = 0
for i in range(L,R+1):
  if i%d==0:
    count = count + 1
print(count)