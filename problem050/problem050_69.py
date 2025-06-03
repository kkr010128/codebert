l = []
while True:
  h,w = map(int,input().split())
  if (h,w) == (0,0):
    break
  else:
    l.append([h,w])
for i in l:
  print('#'*i[1])
  for j in range(i[0]-2):
    print('#'+'.'*(i[1]-2)+'#')
  print('#'*i[1])
  print()