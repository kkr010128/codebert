beforex_plus_y=[]
beforex_minus_y=[]
for i in range(int(input())):
  xy=list(map(int,input().split()))
  beforex_plus_y.append(xy[0]+xy[1])
  beforex_minus_y.append(xy[0]-xy[1])

print(max(max(beforex_plus_y)-min(beforex_plus_y),max(beforex_minus_y)-min(beforex_minus_y)))