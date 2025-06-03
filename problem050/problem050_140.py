data_h = []
data_w = []
while True:
  h, w = (int(i) for i in input().split())
  if h == w == 0:
    break
  else:
    data_h.append(h)
    data_w.append(w)

for i in range(len(data_h)):
  h = data_h[i]
  w = data_w[i]
  for j in range(1,h+1):
    for k in range(1,w+1):
      if j == 1 or j == h or k == 1 or k == w:
        print('#',end='')
      else:
        print('.',end='')
    print('')
  print('')