N,M = map(int,input().split())
tower = list(map(int,input().split()))
road = [list(map(int,input().split())) for i in range(M)]
aa = ['.']*N
for i in road:
  if tower[i[0]-1] > tower[i[1]-1]:
    aa[i[1]-1] = 'v'
  elif tower[i[0]-1] == tower[i[1]-1]:
    aa[i[0]-1] = aa[i[1]-1] = 'v'
  else:
    aa[i[0]-1] = 'v'
print(aa.count('.'))