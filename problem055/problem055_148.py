a=[list(map(int,input().split()))for i in range(int(input()))]
b=[[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in a:
  b[i[0]-1][i[1]-1][i[2]-1] += i[3]
f=0
for i in b:
  if f:print('#'*20)
  else:f=1
  for j in i:
    print('',*j)