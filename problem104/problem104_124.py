L,S,R = map(int,input().split())
a = 0
for i in range(L,S+1):
  if (i%R == 0):
    a = a + 1
print(a)